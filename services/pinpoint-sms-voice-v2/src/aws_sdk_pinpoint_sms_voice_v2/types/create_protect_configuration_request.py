"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateProtectConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateProtectConfigurationRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    deletion_protection_enabled: NotRequired["bool"]
    """<p>When set to true deletion protection is enabled. By default this is set to false. </p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProtectConfigurationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProtectConfigurationRequest:
    out: CreateProtectConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
