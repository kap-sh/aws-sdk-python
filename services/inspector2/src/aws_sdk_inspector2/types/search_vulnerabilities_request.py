"""Generated from Smithy shape ``com.amazonaws.inspector2#SearchVulnerabilitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.next_token
    import aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria


class SearchVulnerabilitiesRequest(TypedDict):
    filter_criteria: "aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria.SearchVulnerabilitiesFilterCriteria"
    """<p>The criteria used to filter the results of a vulnerability search.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVulnerabilitiesRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria

    out["filterCriteria"] = (
        aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchVulnerabilitiesRequest:
    out: SearchVulnerabilitiesRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "SearchVulnerabilitiesRequest.filter_criteria required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
