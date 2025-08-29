from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

def main():
    extractor = Extractor(Config.INPUT_PATH)
    df = extractor.extract()
    if df is None:
        print("No se pudieron extraer los datos.")
        return

    transformer = Transformer(df)
    clean_df = transformer.clean()

    loader = Loader(clean_df)
    loader.to_csv(Config.OUTPUT_PATH)

if __name__ == "__main__":
    main()
