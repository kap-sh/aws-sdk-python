"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListSupplementalTaxRegistrationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.max_results
    import aws_sdk_taxsettings.types.pagination_token_string


class ListSupplementalTaxRegistrationsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_taxsettings.types.max_results.MaxResults"]
    """<p> The number of <code>taxRegistrations</code> results you want in one response. </p>"""
    next_token: NotRequired[
        "aws_sdk_taxsettings.types.pagination_token_string.PaginationTokenString"
    ]
    """<p> The token to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupplementalTaxRegistrationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupplementalTaxRegistrationsRequest:
    out: ListSupplementalTaxRegistrationsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
