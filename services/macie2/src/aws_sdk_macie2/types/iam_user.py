"""Generated from Smithy shape ``com.amazonaws.macie2#IamUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class IamUser(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that's associated with the IAM user who performed the action.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the principal that performed the action. The last section of the ARN contains the name of the user who performed the action.</p>"""
    principal_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the IAM user who performed the action.</p>"""
    user_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The username of the IAM user who performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamUser) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> IamUser:
    out: IamUser = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    if "userName" in data:
        out["user_name"] = data["userName"]
    return out
