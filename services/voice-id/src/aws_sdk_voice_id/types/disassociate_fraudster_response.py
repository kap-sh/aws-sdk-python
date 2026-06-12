"""Generated from Smithy shape ``com.amazonaws.voiceid#DisassociateFraudsterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.fraudster


class DisassociateFraudsterResponse(TypedDict):
    fraudster: NotRequired["aws_sdk_voice_id.types.fraudster.Fraudster"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateFraudsterResponse) -> dict:
    out: dict = {}
    if "fraudster" in value:
        import aws_sdk_voice_id.types.fraudster

        out["Fraudster"] = aws_sdk_voice_id.types.fraudster.serialize_aws_json_1_0(
            value["fraudster"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateFraudsterResponse:
    out: DisassociateFraudsterResponse = {}  # type: ignore[typeddict-item]
    if "Fraudster" in data:
        import aws_sdk_voice_id.types.fraudster

        out["fraudster"] = aws_sdk_voice_id.types.fraudster.deserialize_aws_json_1_0(
            data["Fraudster"]
        )
    return out
