"""Generated from Smithy shape ``com.amazonaws.securityhub#ActorUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.user_account


class ActorUser(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the threat actor. </p>"""
    uid: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The unique identifier of the threat actor. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The type of user. </p>"""
    credential_uid: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Unique identifier of the threat actor’s user credentials. </p>"""
    account: NotRequired["aws_sdk_securityhub.types.user_account.UserAccount"]
    """<p> The account of the threat actor. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActorUser) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "type" in value:
        out["Type"] = value["type"]
    if "credential_uid" in value:
        out["CredentialUid"] = value["credential_uid"]
    if "account" in value:
        import aws_sdk_securityhub.types.user_account

        out["Account"] = aws_sdk_securityhub.types.user_account.serialize_json(
            value["account"]
        )
    return out


def deserialize_json(data: dict) -> ActorUser:
    out: ActorUser = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Uid" in data:
        out["uid"] = data["Uid"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "CredentialUid" in data:
        out["credential_uid"] = data["CredentialUid"]
    if "Account" in data:
        import aws_sdk_securityhub.types.user_account

        out["account"] = aws_sdk_securityhub.types.user_account.deserialize_json(
            data["Account"]
        )
    return out
