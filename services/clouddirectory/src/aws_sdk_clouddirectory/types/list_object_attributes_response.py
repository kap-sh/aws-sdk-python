"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListObjectAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.next_token


class ListObjectAttributesResponse(TypedDict):
    attributes: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>Attributes map that is associated with the object. <code>AttributeArn</code> is the key, and attribute value is the value.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["Attributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListObjectAttributesResponse:
    out: ListObjectAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["Attributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
