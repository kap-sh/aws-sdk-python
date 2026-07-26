"""Generated from Smithy shape ``com.amazonaws.sesv2#ListSuppressedDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.next_token
    import capo_sesv2.types.suppressed_destination_summaries


class ListSuppressedDestinationsResponse(TypedDict, closed=True):
    suppressed_destination_summaries: NotRequired[
        "capo_sesv2.types.suppressed_destination_summaries.SuppressedDestinationSummaries"
    ]
    """<p>A list of summaries, each containing a summary for a suppressed email destination.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional email addresses on the suppression list for your account or for the specified tenant. To view additional suppressed addresses, issue another request to <code>ListSuppressedDestinations</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSuppressedDestinationsResponse) -> dict:
    out: dict = {}
    if "suppressed_destination_summaries" in value:
        import capo_sesv2.types.suppressed_destination_summaries

        out["SuppressedDestinationSummaries"] = (
            capo_sesv2.types.suppressed_destination_summaries.serialize_json(
                value["suppressed_destination_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSuppressedDestinationsResponse:
    out: ListSuppressedDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "SuppressedDestinationSummaries" in data:
        import capo_sesv2.types.suppressed_destination_summaries

        out["suppressed_destination_summaries"] = (
            capo_sesv2.types.suppressed_destination_summaries.deserialize_json(
                data["SuppressedDestinationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
