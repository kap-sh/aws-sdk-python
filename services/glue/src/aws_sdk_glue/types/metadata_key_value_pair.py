"""Generated from Smithy shape ``com.amazonaws.glue#MetadataKeyValuePair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.metadata_key_string
    import aws_sdk_glue.types.metadata_value_string


class MetadataKeyValuePair(TypedDict):
    metadata_key: NotRequired[
        "aws_sdk_glue.types.metadata_key_string.MetadataKeyString"
    ]
    """<p>A metadata key.</p>"""
    metadata_value: NotRequired[
        "aws_sdk_glue.types.metadata_value_string.MetadataValueString"
    ]
    """<p>A metadata key’s corresponding value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataKeyValuePair) -> dict:
    out: dict = {}
    if "metadata_key" in value:
        out["MetadataKey"] = value["metadata_key"]
    if "metadata_value" in value:
        out["MetadataValue"] = value["metadata_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataKeyValuePair:
    out: MetadataKeyValuePair = {}  # type: ignore[typeddict-item]
    if "MetadataKey" in data:
        out["metadata_key"] = data["MetadataKey"]
    if "MetadataValue" in data:
        out["metadata_value"] = data["MetadataValue"]
    return out
