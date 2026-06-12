"""Generated from Smithy shape ``com.amazonaws.connect#DescribeInstanceAttributeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attribute


class DescribeInstanceAttributeResponse(TypedDict):
    attribute: NotRequired["aws_sdk_connect.types.attribute.Attribute"]
    """<p>The type of attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceAttributeResponse) -> dict:
    out: dict = {}
    if "attribute" in value:
        import aws_sdk_connect.types.attribute

        out["Attribute"] = aws_sdk_connect.types.attribute.serialize_json(
            value["attribute"]
        )
    return out


def deserialize_json(data: dict) -> DescribeInstanceAttributeResponse:
    out: DescribeInstanceAttributeResponse = {}  # type: ignore[typeddict-item]
    if "Attribute" in data:
        import aws_sdk_connect.types.attribute

        out["attribute"] = aws_sdk_connect.types.attribute.deserialize_json(
            data["Attribute"]
        )
    return out
