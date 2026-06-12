"""Generated from Smithy shape ``com.amazonaws.connect#ListInstanceAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attributes_list
    import aws_sdk_connect.types.next_token


class ListInstanceAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_connect.types.attributes_list.AttributesList"]
    """<p>The attribute types.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstanceAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_connect.types.attributes_list

        out["Attributes"] = aws_sdk_connect.types.attributes_list.serialize_json(
            value["attributes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstanceAttributesResponse:
    out: ListInstanceAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_connect.types.attributes_list

        out["attributes"] = aws_sdk_connect.types.attributes_list.deserialize_json(
            data["Attributes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
