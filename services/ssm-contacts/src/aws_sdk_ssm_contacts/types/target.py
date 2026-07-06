"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.channel_target_info
    import aws_sdk_ssm_contacts.types.contact_target_info


class Target(TypedDict, closed=True):
    channel_target_info: NotRequired[
        "aws_sdk_ssm_contacts.types.channel_target_info.ChannelTargetInfo"
    ]
    """<p>Information about the contact channel that Incident Manager engages.</p>"""
    contact_target_info: NotRequired[
        "aws_sdk_ssm_contacts.types.contact_target_info.ContactTargetInfo"
    ]
    """<p>Information about the contact that Incident Manager engages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Target) -> dict:
    out: dict = {}
    if "channel_target_info" in value:
        import aws_sdk_ssm_contacts.types.channel_target_info

        out["ChannelTargetInfo"] = (
            aws_sdk_ssm_contacts.types.channel_target_info.serialize_aws_json_1_1(
                value["channel_target_info"]
            )
        )
    if "contact_target_info" in value:
        import aws_sdk_ssm_contacts.types.contact_target_info

        out["ContactTargetInfo"] = (
            aws_sdk_ssm_contacts.types.contact_target_info.serialize_aws_json_1_1(
                value["contact_target_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "ChannelTargetInfo" in data:
        import aws_sdk_ssm_contacts.types.channel_target_info

        out["channel_target_info"] = (
            aws_sdk_ssm_contacts.types.channel_target_info.deserialize_aws_json_1_1(
                data["ChannelTargetInfo"]
            )
        )
    if "ContactTargetInfo" in data:
        import aws_sdk_ssm_contacts.types.contact_target_info

        out["contact_target_info"] = (
            aws_sdk_ssm_contacts.types.contact_target_info.deserialize_aws_json_1_1(
                data["ContactTargetInfo"]
            )
        )
    return out
