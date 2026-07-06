"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRcsAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.client_token
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateRcsAgentRequest(TypedDict, closed=True):
    deletion_protection_enabled: NotRequired["bool"]
    """<p>By default this is set to false. When set to true the RCS agent can't be deleted. You can change this value using the <a>UpdateRcsAgent</a> action.</p>"""
    opt_out_list_name: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    ]
    """<p>The OptOutList to associate with the RCS agent. Valid values are either OptOutListName or OptOutListArn.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) associated with the RCS agent.</p>"""
    client_token: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRcsAgentRequest) -> dict:
    out: dict = {}
    if "deletion_protection_enabled" in value:
        out["DeletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "opt_out_list_name" in value:
        out["OptOutListName"] = value["opt_out_list_name"]
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


def deserialize_aws_json_1_0(data: dict) -> CreateRcsAgentRequest:
    out: CreateRcsAgentRequest = {}  # type: ignore[typeddict-item]
    if "DeletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["DeletionProtectionEnabled"]
    if "OptOutListName" in data:
        out["opt_out_list_name"] = data["OptOutListName"]
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
