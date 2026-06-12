"""Generated from Smithy shape ``com.amazonaws.voiceid#DisassociateFraudsterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.fraudster_id
    import aws_sdk_voice_id.types.watchlist_id


class DisassociateFraudsterRequest(TypedDict):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster.</p>"""
    watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist that you want to disassociate from the fraudster.</p>"""
    fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId"
    """<p>The identifier of the fraudster to be disassociated from the watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateFraudsterRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    out["FraudsterId"] = value["fraudster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateFraudsterRequest:
    out: DisassociateFraudsterRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DisassociateFraudsterRequest.domain_id required")
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        raise DeserializationError("DisassociateFraudsterRequest.watchlist_id required")
    if "FraudsterId" in data:
        out["fraudster_id"] = data["FraudsterId"]
    else:
        raise DeserializationError("DisassociateFraudsterRequest.fraudster_id required")
    return out
