# from energyplus_pet.configure import configure_cli as pet_configure
# from energyplus_regressions.configure import configure_cli as regressions_configure
from eplaunch.configure import configure_cli as launch_configure

def configure_cli() -> None:
    # OK, so for most users, we really don't need to configure shortcuts to all these dev tools
    # It will probably just be like... IDF/EpJSON Editor and EP Launch?
    launch_configure()
    # so for now that's it I guess...we could add a command line argument like --dev which sets up dev tools
    # if len(argv) > 1 and argv[1] == '--dev':
    #   pet_configure
    #   regressions_configure
