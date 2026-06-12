"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListDomainsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.domain_summary_list
    import aws_sdk_codeartifact.types.pagination_token


class ListDomainsResult(TypedDict):
    domains: NotRequired[
        "aws_sdk_codeartifact.types.domain_summary_list.DomainSummaryList"
    ]
    """<p> The returned list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainSummary.html\">DomainSummary</a> objects. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsResult) -> dict:
    out: dict = {}
    if "domains" in value:
        import aws_sdk_codeartifact.types.domain_summary_list

        out["domains"] = aws_sdk_codeartifact.types.domain_summary_list.serialize_json(
            value["domains"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsResult:
    out: ListDomainsResult = {}  # type: ignore[typeddict-item]
    if "domains" in data:
        import aws_sdk_codeartifact.types.domain_summary_list

        out["domains"] = (
            aws_sdk_codeartifact.types.domain_summary_list.deserialize_json(
                data["domains"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
