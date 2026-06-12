"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTableAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attribute_list
    import aws_sdk_connect.types.next_token


class ListDataTableAttributesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    attributes: "aws_sdk_connect.types.attribute_list.AttributeList"
    """<p>A list of data table attributes with their complete configuration and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTableAttributesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_connect.types.attribute_list

    out["Attributes"] = aws_sdk_connect.types.attribute_list.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> ListDataTableAttributesResponse:
    out: ListDataTableAttributesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Attributes" in data:
        import aws_sdk_connect.types.attribute_list

        out["attributes"] = aws_sdk_connect.types.attribute_list.deserialize_json(
            data["Attributes"]
        )
    else:
        raise DeserializationError(
            "ListDataTableAttributesResponse.attributes required"
        )
    return out
