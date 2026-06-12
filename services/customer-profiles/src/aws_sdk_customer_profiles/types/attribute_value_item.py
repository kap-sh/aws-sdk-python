"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeValueItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255


class AttributeValueItem(TypedDict):
    value: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>An individual value belonging to the given attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueItem) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AttributeValueItem:
    out: AttributeValueItem = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
