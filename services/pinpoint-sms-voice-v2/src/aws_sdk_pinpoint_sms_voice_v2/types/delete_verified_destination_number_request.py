"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteVerifiedDestinationNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn


class DeleteVerifiedDestinationNumberRequest(TypedDict, closed=True):
    verified_destination_number_id: "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn"
    """<p>The unique identifier for the verified destination phone number.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVerifiedDestinationNumberRequest) -> dict:
    out: dict = {}
    out["VerifiedDestinationNumberId"] = value["verified_destination_number_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVerifiedDestinationNumberRequest:
    out: DeleteVerifiedDestinationNumberRequest = {}  # type: ignore[typeddict-item]
    if "VerifiedDestinationNumberId" in data:
        out["verified_destination_number_id"] = data["VerifiedDestinationNumberId"]
    else:
        raise DeserializationError(
            "DeleteVerifiedDestinationNumberRequest.verified_destination_number_id required"
        )
    return out
