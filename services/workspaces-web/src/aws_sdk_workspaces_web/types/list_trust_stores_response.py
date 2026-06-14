"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListTrustStoresResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.trust_store_summary_list


class ListTrustStoresResponse(TypedDict):
    trust_stores: NotRequired[
        "aws_sdk_workspaces_web.types.trust_store_summary_list.TrustStoreSummaryList"
    ]
    """<p>The trust stores.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustStoresResponse) -> dict:
    out: dict = {}
    if "trust_stores" in value:
        import aws_sdk_workspaces_web.types.trust_store_summary_list

        out["trustStores"] = (
            aws_sdk_workspaces_web.types.trust_store_summary_list.serialize_json(
                value["trust_stores"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrustStoresResponse:
    out: ListTrustStoresResponse = {}  # type: ignore[typeddict-item]
    if "trustStores" in data:
        import aws_sdk_workspaces_web.types.trust_store_summary_list

        out["trust_stores"] = (
            aws_sdk_workspaces_web.types.trust_store_summary_list.deserialize_json(
                data["trustStores"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
