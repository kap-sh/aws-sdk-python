"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.after_contact_work_configs
    import aws_sdk_connect.types.auto_accept_configs
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.persistent_connection_configs
    import aws_sdk_connect.types.phone_number_configs
    import aws_sdk_connect.types.user_id
    import aws_sdk_connect.types.voice_enhancement_configs


class UpdateUserConfigRequest(TypedDict):
    auto_accept_configs: NotRequired[
        "aws_sdk_connect.types.auto_accept_configs.AutoAcceptConfigs"
    ]
    """<p>The list of auto-accept configuration settings for each channel. When auto-accept is enabled for a channel, available agents are automatically connected to contacts from that channel without needing to manually accept. Auto-accept connects agents to contacts in less than one second.</p>"""
    after_contact_work_configs: NotRequired[
        "aws_sdk_connect.types.after_contact_work_configs.AfterContactWorkConfigs"
    ]
    """<p>The list of after contact work (ACW) timeout configuration settings for each channel. ACW timeout specifies how many seconds agents have for after contact work, such as entering notes about the contact. The minimum setting is 1 second, and the maximum is 2,000,000 seconds (24 days). Enter 0 for an indefinite amount of time, meaning agents must manually choose to end ACW.</p>"""
    phone_number_configs: NotRequired[
        "aws_sdk_connect.types.phone_number_configs.PhoneNumberConfigs"
    ]
    """<p>The list of phone number configuration settings for each channel.</p>"""
    persistent_connection_configs: NotRequired[
        "aws_sdk_connect.types.persistent_connection_configs.PersistentConnectionConfigs"
    ]
    """<p>The list of persistent connection configuration settings for each channel.</p>"""
    voice_enhancement_configs: NotRequired[
        "aws_sdk_connect.types.voice_enhancement_configs.VoiceEnhancementConfigs"
    ]
    """<p>The list of voice enhancement configuration settings for each channel.</p>"""
    user_id: "aws_sdk_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserConfigRequest) -> dict:
    out: dict = {}
    if "auto_accept_configs" in value:
        import aws_sdk_connect.types.auto_accept_configs

        out["AutoAcceptConfigs"] = (
            aws_sdk_connect.types.auto_accept_configs.serialize_json(
                value["auto_accept_configs"]
            )
        )
    if "after_contact_work_configs" in value:
        import aws_sdk_connect.types.after_contact_work_configs

        out["AfterContactWorkConfigs"] = (
            aws_sdk_connect.types.after_contact_work_configs.serialize_json(
                value["after_contact_work_configs"]
            )
        )
    if "phone_number_configs" in value:
        import aws_sdk_connect.types.phone_number_configs

        out["PhoneNumberConfigs"] = (
            aws_sdk_connect.types.phone_number_configs.serialize_json(
                value["phone_number_configs"]
            )
        )
    if "persistent_connection_configs" in value:
        import aws_sdk_connect.types.persistent_connection_configs

        out["PersistentConnectionConfigs"] = (
            aws_sdk_connect.types.persistent_connection_configs.serialize_json(
                value["persistent_connection_configs"]
            )
        )
    if "voice_enhancement_configs" in value:
        import aws_sdk_connect.types.voice_enhancement_configs

        out["VoiceEnhancementConfigs"] = (
            aws_sdk_connect.types.voice_enhancement_configs.serialize_json(
                value["voice_enhancement_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateUserConfigRequest:
    out: UpdateUserConfigRequest = {}  # type: ignore[typeddict-item]
    if "AutoAcceptConfigs" in data:
        import aws_sdk_connect.types.auto_accept_configs

        out["auto_accept_configs"] = (
            aws_sdk_connect.types.auto_accept_configs.deserialize_json(
                data["AutoAcceptConfigs"]
            )
        )
    if "AfterContactWorkConfigs" in data:
        import aws_sdk_connect.types.after_contact_work_configs

        out["after_contact_work_configs"] = (
            aws_sdk_connect.types.after_contact_work_configs.deserialize_json(
                data["AfterContactWorkConfigs"]
            )
        )
    if "PhoneNumberConfigs" in data:
        import aws_sdk_connect.types.phone_number_configs

        out["phone_number_configs"] = (
            aws_sdk_connect.types.phone_number_configs.deserialize_json(
                data["PhoneNumberConfigs"]
            )
        )
    if "PersistentConnectionConfigs" in data:
        import aws_sdk_connect.types.persistent_connection_configs

        out["persistent_connection_configs"] = (
            aws_sdk_connect.types.persistent_connection_configs.deserialize_json(
                data["PersistentConnectionConfigs"]
            )
        )
    if "VoiceEnhancementConfigs" in data:
        import aws_sdk_connect.types.voice_enhancement_configs

        out["voice_enhancement_configs"] = (
            aws_sdk_connect.types.voice_enhancement_configs.deserialize_json(
                data["VoiceEnhancementConfigs"]
            )
        )
    return out
