"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListChangeSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.change_set_summary_list
    import aws_sdk_marketplace_catalog.types.next_token


class ListChangeSetsResponse(TypedDict):
    change_set_summary_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.change_set_summary_list.ChangeSetSummaryList"
    ]
    """<p> Array of <code>ChangeSetSummaryListItem</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. Null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangeSetsResponse) -> dict:
    out: dict = {}
    if "change_set_summary_list" in value:
        import aws_sdk_marketplace_catalog.types.change_set_summary_list

        out["ChangeSetSummaryList"] = (
            aws_sdk_marketplace_catalog.types.change_set_summary_list.serialize_json(
                value["change_set_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangeSetsResponse:
    out: ListChangeSetsResponse = {}  # type: ignore[typeddict-item]
    if "ChangeSetSummaryList" in data:
        import aws_sdk_marketplace_catalog.types.change_set_summary_list

        out["change_set_summary_list"] = (
            aws_sdk_marketplace_catalog.types.change_set_summary_list.deserialize_json(
                data["ChangeSetSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
