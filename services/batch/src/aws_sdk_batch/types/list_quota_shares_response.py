"""Generated from Smithy shape ``com.amazonaws.batch#ListQuotaSharesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_list
    import aws_sdk_batch.types.string


class ListQuotaSharesResponse(TypedDict, closed=True):
    quota_shares: NotRequired["aws_sdk_batch.types.quota_share_list.QuotaShareList"]
    """<p>A list of quota shares that match the request.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListQuotaShares</code> request. When the results of a <code>ListQuotaShares</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuotaSharesResponse) -> dict:
    out: dict = {}
    if "quota_shares" in value:
        import aws_sdk_batch.types.quota_share_list

        out["quotaShares"] = aws_sdk_batch.types.quota_share_list.serialize_json(
            value["quota_shares"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuotaSharesResponse:
    out: ListQuotaSharesResponse = {}  # type: ignore[typeddict-item]
    if "quotaShares" in data:
        import aws_sdk_batch.types.quota_share_list

        out["quota_shares"] = aws_sdk_batch.types.quota_share_list.deserialize_json(
            data["quotaShares"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
