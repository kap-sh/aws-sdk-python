"""Generated from Smithy shape ``com.amazonaws.ssm#MetadataValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.metadata_value_string


class MetadataValue(TypedDict, closed=True):
    value: NotRequired["aws_sdk_ssm.types.metadata_value_string.MetadataValueString"]
    """<p>Metadata value to assign to an Application Manager application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataValue:
    out: MetadataValue = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
