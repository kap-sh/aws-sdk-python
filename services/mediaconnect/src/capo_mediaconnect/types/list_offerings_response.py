"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_offering


class ListOfferingsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>"""
    offerings: NotRequired[
        "capo_mediaconnect.types.__list_of_offering.__listOfOffering"
    ]
    """<p> A list of offerings that are available to this account in the current Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOfferingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "offerings" in value:
        import capo_mediaconnect.types.__list_of_offering

        out["offerings"] = capo_mediaconnect.types.__list_of_offering.serialize_json(
            value["offerings"]
        )
    return out


def deserialize_json(data: dict) -> ListOfferingsResponse:
    out: ListOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "offerings" in data:
        import capo_mediaconnect.types.__list_of_offering

        out["offerings"] = capo_mediaconnect.types.__list_of_offering.deserialize_json(
            data["offerings"]
        )
    return out
