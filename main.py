from libretranslate import main
import pathlib
import argostranslate.package as package
import traceback

package_path_en_vi = pathlib.Path("/app/vi/translate-en_vi-1_0.argosmodel")
package_path_vi_en = pathlib.Path("/app/vi/translate-vi_en-1_0.argosmodel")

def install_model(path):
    try:
        package.install_from_path(path)
        print(f"[OK] Installed model: {path.name}")
    except Exception as e:
        print(f"[FAIL] Could not install model {path.name}")
        traceback.print_exc()
        
install_model(package_path_en_vi)
install_model(package_path_vi_en)


if __name__ == "__main__":
    main()



