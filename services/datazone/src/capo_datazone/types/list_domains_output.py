"""Generated from Smithy shape ``com.amazonaws.datazone#ListDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_summaries
    import capo_datazone.types.pagination_token


class ListDomainsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.domain_summaries.DomainSummaries"
    """<p>The results of the <code>ListDomains</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.domain_summaries

    out["items"] = capo_datazone.types.domain_summaries.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsOutput:
    out: ListDomainsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_datazone.types.domain_summaries

        out["items"] = capo_datazone.types.domain_summaries.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListDomainsOutput.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
