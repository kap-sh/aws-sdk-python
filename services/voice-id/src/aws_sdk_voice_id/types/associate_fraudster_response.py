"""Generated from Smithy shape ``com.amazonaws.voiceid#AssociateFraudsterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.fraudster


class AssociateFraudsterResponse(TypedDict, closed=True):
    fraudster: NotRequired["aws_sdk_voice_id.types.fraudster.Fraudster"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateFraudsterResponse) -> dict:
    out: dict = {}
    if "fraudster" in value:
        import aws_sdk_voice_id.types.fraudster

        out["Fraudster"] = aws_sdk_voice_id.types.fraudster.serialize_aws_json_1_0(
            value["fraudster"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateFraudsterResponse:
    out: AssociateFraudsterResponse = {}  # type: ignore[typeddict-item]
    if "Fraudster" in data:
        import aws_sdk_voice_id.types.fraudster

        out["fraudster"] = aws_sdk_voice_id.types.fraudster.deserialize_aws_json_1_0(
            data["Fraudster"]
        )
    return out
