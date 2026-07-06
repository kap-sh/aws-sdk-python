"""Generated from Smithy shape ``com.amazonaws.voiceid#FraudsterSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.generated_fraudster_id
    import aws_sdk_voice_id.types.response_watchlist_ids
    import aws_sdk_voice_id.types.timestamp


class FraudsterSummary(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the fraudster summary.</p>"""
    generated_fraudster_id: NotRequired[
        "aws_sdk_voice_id.types.generated_fraudster_id.GeneratedFraudsterId"
    ]
    """<p>The service-generated identifier for the fraudster.</p>"""
    created_at: NotRequired["aws_sdk_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the fraudster summary was created.</p>"""
    watchlist_ids: NotRequired[
        "aws_sdk_voice_id.types.response_watchlist_ids.ResponseWatchlistIds"
    ]
    """<p>The identifier of the watchlists the fraudster is a part of.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FraudsterSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "generated_fraudster_id" in value:
        out["GeneratedFraudsterId"] = value["generated_fraudster_id"]
    if "created_at" in value:
        import aws_sdk_voice_id.types.timestamp

        out["CreatedAt"] = aws_sdk_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "watchlist_ids" in value:
        import aws_sdk_voice_id.types.response_watchlist_ids

        out["WatchlistIds"] = (
            aws_sdk_voice_id.types.response_watchlist_ids.serialize_aws_json_1_0(
                value["watchlist_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FraudsterSummary:
    out: FraudsterSummary = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "GeneratedFraudsterId" in data:
        out["generated_fraudster_id"] = data["GeneratedFraudsterId"]
    if "CreatedAt" in data:
        import aws_sdk_voice_id.types.timestamp

        out["created_at"] = aws_sdk_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "WatchlistIds" in data:
        import aws_sdk_voice_id.types.response_watchlist_ids

        out["watchlist_ids"] = (
            aws_sdk_voice_id.types.response_watchlist_ids.deserialize_aws_json_1_0(
                data["WatchlistIds"]
            )
        )
    return out
