"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListFacetAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet_attribute_list
    import aws_sdk_clouddirectory.types.next_token


class ListFacetAttributesResponse(TypedDict):
    attributes: NotRequired[
        "aws_sdk_clouddirectory.types.facet_attribute_list.FacetAttributeList"
    ]
    """<p>The attributes attached to the facet.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFacetAttributesResponse) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_clouddirectory.types.facet_attribute_list

        out["Attributes"] = (
            aws_sdk_clouddirectory.types.facet_attribute_list.serialize_json(
                value["attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFacetAttributesResponse:
    out: ListFacetAttributesResponse = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_clouddirectory.types.facet_attribute_list

        out["attributes"] = (
            aws_sdk_clouddirectory.types.facet_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
