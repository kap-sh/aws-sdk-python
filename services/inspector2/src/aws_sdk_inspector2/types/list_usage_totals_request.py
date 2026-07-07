"""Generated from Smithy shape ``com.amazonaws.inspector2#ListUsageTotalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.list_usage_totals_max_results
    import aws_sdk_inspector2.types.list_usage_totals_next_token
    import aws_sdk_inspector2.types.usage_account_id_list


class ListUsageTotalsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_inspector2.types.list_usage_totals_max_results.ListUsageTotalsMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""
    next_token: NotRequired[
        "aws_sdk_inspector2.types.list_usage_totals_next_token.ListUsageTotalsNextToken"
    ]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    account_ids: NotRequired[
        "aws_sdk_inspector2.types.usage_account_id_list.UsageAccountIdList"
    ]
    """<p>The Amazon Web Services account IDs to retrieve usage totals for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsageTotalsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_ids" in value:
        import aws_sdk_inspector2.types.usage_account_id_list

        out["accountIds"] = (
            aws_sdk_inspector2.types.usage_account_id_list.serialize_json(
                value["account_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListUsageTotalsRequest:
    out: ListUsageTotalsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.usage_account_id_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.usage_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    return out
