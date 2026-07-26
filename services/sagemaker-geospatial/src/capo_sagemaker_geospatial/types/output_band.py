"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OutputBand``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.output_type


class OutputBand(TypedDict, closed=True):
    band_name: "str"
    """<p>The name of the band.</p>"""
    output_data_type: "capo_sagemaker_geospatial.types.output_type.OutputType"
    """<p>The datatype of the output band.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputBand) -> dict:
    out: dict = {}
    out["BandName"] = value["band_name"]
    out["OutputDataType"] = value["output_data_type"]
    return out


def deserialize_json(data: dict) -> OutputBand:
    out: OutputBand = {}  # type: ignore[typeddict-item]
    if "BandName" in data:
        out["band_name"] = data["BandName"]
    else:
        raise DeserializationError("OutputBand.band_name required")
    if "OutputDataType" in data:
        out["output_data_type"] = data["OutputDataType"]
    else:
        raise DeserializationError("OutputBand.output_data_type required")
    return out
