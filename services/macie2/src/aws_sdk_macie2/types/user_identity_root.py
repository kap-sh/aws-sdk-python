"""Generated from Smithy shape ``com.amazonaws.macie2#UserIdentityRoot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class UserIdentityRoot(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user or role that performed the action.</p>"""
    principal_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the entity that performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentityRoot) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    return out


def deserialize_json(data: dict) -> UserIdentityRoot:
    out: UserIdentityRoot = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    return out
