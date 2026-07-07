"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_summary_list
    import aws_sdk_controlcatalog.types.pagination_token


class ListDomainsResponse(TypedDict, closed=True):
    domains: "aws_sdk_controlcatalog.types.domain_summary_list.DomainSummaryList"
    """<p>The list of domains that the <code>ListDomains</code> API returns.</p>"""
    next_token: NotRequired[
        "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsResponse) -> dict:
    out: dict = {}
    import aws_sdk_controlcatalog.types.domain_summary_list

    out["Domains"] = aws_sdk_controlcatalog.types.domain_summary_list.serialize_json(
        value["domains"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if "Domains" in data:
        import aws_sdk_controlcatalog.types.domain_summary_list

        out["domains"] = (
            aws_sdk_controlcatalog.types.domain_summary_list.deserialize_json(
                data["Domains"]
            )
        )
    else:
        raise DeserializationError("ListDomainsResponse.domains required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
