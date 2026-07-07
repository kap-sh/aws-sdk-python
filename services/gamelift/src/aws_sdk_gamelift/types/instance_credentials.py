"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_empty_string


class InstanceCredentials(TypedDict, closed=True):
    user_name: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A user name for logging in.</p>"""
    secret: NotRequired["aws_sdk_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>Secret string. For Windows instances, the secret is a password for use with Windows Remote Desktop. For Linux instances, it's a private key for use with SSH.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceCredentials) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "secret" in value:
        out["Secret"] = value["secret"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceCredentials:
    out: InstanceCredentials = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Secret" in data:
        out["secret"] = data["Secret"]
    return out
