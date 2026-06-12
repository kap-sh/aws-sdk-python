"""Generated from Smithy shape ``com.amazonaws.memorydb#ParameterNameValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class ParameterNameValue(TypedDict):
    parameter_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the parameter</p>"""
    parameter_value: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The value of the parameter</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameValue) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterNameValue:
    out: ParameterNameValue = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "ParameterValue" in data:
        out["parameter_value"] = data["ParameterValue"]
    return out
