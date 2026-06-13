"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateConfigurationSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateConfigurationSetRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    """<p>The name to use for the new configuration set.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that's associated with the new configuration set. </p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConfigurationSetRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateConfigurationSetRequest:
    out: CreateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "CreateConfigurationSetRequest.configuration_set_name required"
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
