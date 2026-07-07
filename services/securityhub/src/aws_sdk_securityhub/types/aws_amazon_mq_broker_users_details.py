"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerUsersDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAmazonMqBrokerUsersDetails(TypedDict, closed=True):
    pending_change: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of change pending for the broker user. </p>"""
    username: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The username of the broker user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerUsersDetails) -> dict:
    out: dict = {}
    if "pending_change" in value:
        out["PendingChange"] = value["pending_change"]
    if "username" in value:
        out["Username"] = value["username"]
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerUsersDetails:
    out: AwsAmazonMqBrokerUsersDetails = {}  # type: ignore[typeddict-item]
    if "PendingChange" in data:
        out["pending_change"] = data["PendingChange"]
    if "Username" in data:
        out["username"] = data["Username"]
    return out
