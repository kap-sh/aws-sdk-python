"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateRegistrationRequest(TypedDict):
    registration_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form to create. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the registration.</p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationRequest) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationRequest:
    out: CreateRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationType" in data:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "CreateRegistrationRequest.registration_type required"
        )
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
