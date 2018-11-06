from astropy.table import Table

from specutils.io.registers import data_loader


# Do we want an indentifier here?

@data_loader(label="{name}")
def simple_generic_loader(file_name, **kwargs):

    # Use name of the file for the spectra object that's created
    # when the data is loaded.
    name = os.path.basename(file_name.rstrip(os.sep)).rsplit('.', 1)[0]

    ast_table = Table.read(file_name, **kwargs)

    flux = ast_table['{data_col}']
    wavelength = ast_table['{dispersion_col}']

    # Set units
    unit = Unit("{data_unit}")
    disp_unit = Unit("{dispersion_unit}")

    # A new spectrum object is returned, which specviz understands
    return Spectrum1D(spectral_axis=wavelength * disp_unit, flux=flux * unit,
                      meta=header)

