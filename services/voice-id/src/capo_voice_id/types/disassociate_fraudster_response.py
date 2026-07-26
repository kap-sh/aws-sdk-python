"""Generated from Smithy shape ``com.amazonaws.voiceid#DisassociateFraudsterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.fraudster


class DisassociateFraudsterResponse(TypedDict, closed=True):
    fraudster: NotRequired["capo_voice_id.types.fraudster.Fraudster"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateFraudsterResponse) -> dict:
    out: dict = {}
    if "fraudster" in value:
        import capo_voice_id.types.fraudster

        out["Fraudster"] = capo_voice_id.types.fraudster.serialize_aws_json_1_0(
            value["fraudster"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateFraudsterResponse:
    out: DisassociateFraudsterResponse = {}  # type: ignore[typeddict-item]
    if "Fraudster" in data:
        import capo_voice_id.types.fraudster

        out["fraudster"] = capo_voice_id.types.fraudster.deserialize_aws_json_1_0(
            data["Fraudster"]
        )
    return out
