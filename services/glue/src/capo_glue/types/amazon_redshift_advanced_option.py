"""Generated from Smithy shape ``com.amazonaws.glue#AmazonRedshiftAdvancedOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string


class AmazonRedshiftAdvancedOption(TypedDict, closed=True):
    key: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The key for the additional connection option.</p>"""
    value: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The value for the additional connection option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonRedshiftAdvancedOption) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonRedshiftAdvancedOption:
    out: AmazonRedshiftAdvancedOption = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
