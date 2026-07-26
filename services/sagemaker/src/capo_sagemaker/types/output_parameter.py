"""Generated from Smithy shape ``com.amazonaws.sagemaker#OutputParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.string1024


class OutputParameter(TypedDict, closed=True):
    name: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The name of the output parameter.</p>"""
    value: NotRequired["capo_sagemaker.types.string1024.String1024"]
    """<p>The value of the output parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputParameter:
    out: OutputParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
