"""Generated from Smithy shape ``com.amazonaws.securitylake#ListLogSourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.account_list
    import aws_sdk_securitylake.types.log_source_resource_list
    import aws_sdk_securitylake.types.max_results
    import aws_sdk_securitylake.types.next_token
    import aws_sdk_securitylake.types.region_list


class ListLogSourcesRequest(TypedDict):
    accounts: NotRequired["aws_sdk_securitylake.types.account_list.AccountList"]
    """<p>The list of Amazon Web Services accounts for which log sources are displayed.</p>"""
    regions: NotRequired["aws_sdk_securitylake.types.region_list.RegionList"]
    """<p>The list of Regions for which log sources are displayed.</p>"""
    sources: NotRequired[
        "aws_sdk_securitylake.types.log_source_resource_list.LogSourceResourceList"
    ]
    """<p>The list of sources for which log sources are displayed.</p>"""
    max_results: "aws_sdk_securitylake.types.max_results.MaxResults"
    """<p>The maximum number of accounts for which the log sources are displayed.</p>"""
    next_token: NotRequired["aws_sdk_securitylake.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLogSourcesRequest) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_securitylake.types.account_list

        out["accounts"] = aws_sdk_securitylake.types.account_list.serialize_json(
            value["accounts"]
        )
    if "regions" in value:
        import aws_sdk_securitylake.types.region_list

        out["regions"] = aws_sdk_securitylake.types.region_list.serialize_json(
            value["regions"]
        )
    if "sources" in value:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.serialize_json(
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
        import aws_sdk_securitylake.types.account_list

        out["accounts"] = aws_sdk_securitylake.types.account_list.deserialize_json(
            data["accounts"]
        )
    if "regions" in data:
        import aws_sdk_securitylake.types.region_list

        out["regions"] = aws_sdk_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    if "sources" in data:
        import aws_sdk_securitylake.types.log_source_resource_list

        out["sources"] = (
            aws_sdk_securitylake.types.log_source_resource_list.deserialize_json(
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
