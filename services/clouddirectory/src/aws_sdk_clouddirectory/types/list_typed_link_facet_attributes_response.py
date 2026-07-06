"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListTypedLinkFacetAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list


class ListTypedLinkFacetAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired[
        "aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.TypedLinkAttributeDefinitionList"
    ]
    """<p>An ordered set of attributes associate with the typed link.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTypedLinkFacetAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list

        out["Attributes"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.serialize_json(
                value["attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTypedLinkFacetAttributesResponse:
    out: ListTypedLinkFacetAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.typed_link_attribute_definition_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.typed_link_attribute_definition_list.deserialize_json(
                data["Attributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
