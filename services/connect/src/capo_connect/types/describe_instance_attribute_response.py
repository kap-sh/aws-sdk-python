"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attribute


class DescribeInstanceAttributeResponse(TypedDict, closed=True):
    attribute: NotRequired["capo_connect.types.attribute.Attribute"]
    """<p>The type of attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceAttributeResponse) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_connect.types.attribute

        out["Attribute"] = capo_connect.types.attribute.serialize_json(
            value["attribute"]
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceAttributeResponse:
    out: DescribeInstanceAttributeResponse = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import capo_connect.types.attribute

        out["attribute"] = capo_connect.types.attribute.deserialize_json(
            data["Attribute"]
        )
    return out
