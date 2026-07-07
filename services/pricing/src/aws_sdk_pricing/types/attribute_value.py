"""Generated from Smithy shape ``com.amazonaws.pricing#AttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pricing.types.string


class AttributeValue(TypedDict, closed=True):
    value: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The specific value of an <code>attributeName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeValue:
    out: AttributeValue = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
