"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccountReceiver``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.alias
    import aws_sdk_partnercentral_selling.types.aws_account


class AccountReceiver(TypedDict):
    alias: NotRequired["aws_sdk_partnercentral_selling.types.alias.Alias"]
    """<p>Represents the alias of the partner account receiving the Engagement Invitation, making it easier to identify and track the recipient in reports or logs.</p>"""
    aws_account_id: "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    """<p>Indicates the AWS account ID of the partner who received the Engagement Invitation. This is a unique identifier for managing engagements with specific AWS accounts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountReceiver) -> dict:
    out: dict = {}
    if "alias" in value:
        out["Alias"] = value["alias"]
    out["AwsAccountId"] = value["aws_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountReceiver:
    out: AccountReceiver = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    else:
        raise DeserializationError("AccountReceiver.aws_account_id required")
    return out
