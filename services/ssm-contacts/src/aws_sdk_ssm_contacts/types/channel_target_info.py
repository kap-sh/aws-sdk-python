"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ChannelTargetInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.retry_interval_in_minutes
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ChannelTargetInfo(TypedDict):
    contact_channel_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""
    retry_interval_in_minutes: NotRequired[
        "aws_sdk_ssm_contacts.types.retry_interval_in_minutes.RetryIntervalInMinutes"
    ]
    """<p>The number of minutes to wait before retrying to send engagement if the engagement initially failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChannelTargetInfo) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    if "retry_interval_in_minutes" in value:
        out["RetryIntervalInMinutes"] = value["retry_interval_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChannelTargetInfo:
    out: ChannelTargetInfo = {}  # type: ignore[typeddict-item]
    if "ContactChannelId" in data:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        raise DeserializationError("ChannelTargetInfo.contact_channel_id required")
    if "RetryIntervalInMinutes" in data:
        out["retry_interval_in_minutes"] = data["RetryIntervalInMinutes"]
    return out
