"""Generated from Smithy shape ``com.amazonaws.securitylake#ListLogSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.account_list
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token
    import capo_securitylake.types.region_list


class ListLogSourcesRequest(TypedDict, closed=True):
    accounts: NotRequired["capo_securitylake.types.account_list.AccountList"]
    """<p>The list of Amazon Web Services accounts for which log sources are displayed.</p>"""
    regions: NotRequired["capo_securitylake.types.region_list.RegionList"]
    """<p>The list of Regions for which log sources are displayed.</p>"""
    sources: NotRequired[
        "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
    ]
    """<p>The list of sources for which log sources are displayed.</p>"""
    max_results: "capo_securitylake.types.max_results.MaxResults"
    """<p>The maximum number of accounts for which the log sources are displayed.</p>"""
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLogSourcesRequest) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.serialize_json(
            value["accounts"]
        )
    if "regions" in value:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.serialize_json(
            value["regions"]
        )
    if "sources" in value:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.serialize_json(
                value["sources"]
            )
        )
    out["maxResults"] = value.get("max_results", 50)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLogSourcesRequest:
    out: ListLogSourcesRequest = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.deserialize_json(
            data["accounts"]
        )
    if "regions" in data:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    if "sources" in data:
        import capo_securitylake.types.log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 50
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
