"""Generated from Smithy shape ``com.amazonaws.quicksight#MappedDataSetParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_identifier
    import aws_sdk_quicksight.types.parameter_name


class MappedDataSetParameter(TypedDict):
    data_set_identifier: (
        "aws_sdk_quicksight.types.data_set_identifier.DataSetIdentifier"
    )
    """<p>A unique name that identifies a dataset within the analysis or dashboard.</p>"""
    data_set_parameter_name: "aws_sdk_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the dataset parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MappedDataSetParameter) -> dict:
    out: dict = {}
    out["DataSetIdentifier"] = value["data_set_identifier"]
    out["DataSetParameterName"] = value["data_set_parameter_name"]
    return out


def deserialize_json(data: dict) -> MappedDataSetParameter:
    out: MappedDataSetParameter = {}  # type: ignore[typeddict-item]
    if "DataSetIdentifier" in data:
        out["data_set_identifier"] = data["DataSetIdentifier"]
    else:
        raise DeserializationError(
            "MappedDataSetParameter.data_set_identifier required"
        )
    if "DataSetParameterName" in data:
        out["data_set_parameter_name"] = data["DataSetParameterName"]
    else:
        raise DeserializationError(
            "MappedDataSetParameter.data_set_parameter_name required"
        )
    return out
