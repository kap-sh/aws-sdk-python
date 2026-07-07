"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListEntitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.entity_summary_list
    import aws_sdk_marketplace_catalog.types.next_token


class ListEntitiesResponse(TypedDict, closed=True):
    entity_summary_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.entity_summary_list.EntitySummaryList"
    ]
    """<p>Array of <code>EntitySummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token if it exists. Null if there is no more result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesResponse) -> dict:
    out: dict = {}
    if "entity_summary_list" in value:
        import aws_sdk_marketplace_catalog.types.entity_summary_list

        out["EntitySummaryList"] = (
            aws_sdk_marketplace_catalog.types.entity_summary_list.serialize_json(
                value["entity_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitiesResponse:
    out: ListEntitiesResponse = {}  # type: ignore[typeddict-item]
    if "EntitySummaryList" in data:
        import aws_sdk_marketplace_catalog.types.entity_summary_list

        out["entity_summary_list"] = (
            aws_sdk_marketplace_catalog.types.entity_summary_list.deserialize_json(
                data["EntitySummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
