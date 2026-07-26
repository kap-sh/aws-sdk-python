"""Generated from Smithy shape ``com.amazonaws.voiceid#Fraudster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.generated_fraudster_id
    import capo_voice_id.types.response_watchlist_ids
    import capo_voice_id.types.timestamp


class Fraudster(TypedDict, closed=True):
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the fraudster.</p>"""
    generated_fraudster_id: NotRequired[
        "capo_voice_id.types.generated_fraudster_id.GeneratedFraudsterId"
    ]
    """<p>The service-generated identifier for the fraudster.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when Voice ID identified the fraudster.</p>"""
    watchlist_ids: NotRequired[
        "capo_voice_id.types.response_watchlist_ids.ResponseWatchlistIds"
    ]
    """<p>The identifier of the watchlists the fraudster is a part of.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Fraudster) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "generated_fraudster_id" in value:
        out["GeneratedFraudsterId"] = value["generated_fraudster_id"]
    if "created_at" in value:
        import capo_voice_id.types.timestamp

        out["CreatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "watchlist_ids" in value:
        import capo_voice_id.types.response_watchlist_ids

        out["WatchlistIds"] = (
            capo_voice_id.types.response_watchlist_ids.serialize_aws_json_1_0(
                value["watchlist_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Fraudster:
    out: Fraudster = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "GeneratedFraudsterId" in data:
        out["generated_fraudster_id"] = data["GeneratedFraudsterId"]
    if "CreatedAt" in data:
        import capo_voice_id.types.timestamp

        out["created_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "WatchlistIds" in data:
        import capo_voice_id.types.response_watchlist_ids

        out["watchlist_ids"] = (
            capo_voice_id.types.response_watchlist_ids.deserialize_aws_json_1_0(
                data["WatchlistIds"]
            )
        )
    return out
