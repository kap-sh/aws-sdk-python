"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateVerifiedDestinationNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateVerifiedDestinationNumberRequest(TypedDict, closed=True):
    destination_phone_number: (
        "aws_sdk_pinpoint_sms_voice_v2.types.phone_number.PhoneNumber"
    )
    """<p>The verified destination phone number, in E.164 format.</p>"""
    rcs_agent_id: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    ]
    """<p>The unique identifier of the RCS agent to associate with the verified destination number. You can use either the RcsAgentId or RcsAgentArn.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the destination number.</p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVerifiedDestinationNumberRequest) -> dict:
    out: dict = {}
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    if "rcs_agent_id" in value:
        out["RcsAgentId"] = value["rcs_agent_id"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVerifiedDestinationNumberRequest:
    out: CreateVerifiedDestinationNumberRequest = {}  # type: ignore[typeddict-item]
    if "DestinationPhoneNumber" in data:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "CreateVerifiedDestinationNumberRequest.destination_phone_number required"
        )
    if "RcsAgentId" in data:
        out["rcs_agent_id"] = data["RcsAgentId"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
