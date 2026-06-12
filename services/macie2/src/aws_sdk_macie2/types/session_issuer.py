"""Generated from Smithy shape ``com.amazonaws.macie2#SessionIssuer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class SessionIssuer(TypedDict):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that owns the entity that was used to get the credentials.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the source account, Identity and Access Management (IAM) user, or role that was used to get the credentials.</p>"""
    principal_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the entity that was used to get the credentials.</p>"""
    type: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The source of the temporary security credentials, such as Root, IAMUser, or Role.</p>"""
    user_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name or alias of the user or role that issued the session. This value is null if the credentials were obtained from a root account that doesn't have an alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionIssuer) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "type" in value:
        out["type"] = value["type"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> SessionIssuer:
    out: SessionIssuer = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "type" in data:
        out["type"] = data["type"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    return out
