"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipAccountDetailError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_account_id


class GetMembershipAccountDetailError(TypedDict, closed=True):
    account_id: "aws_sdk_security_ir.types.aws_account_id.AWSAccountId"
    """<p/>"""
    error: "str"
    """<p/>"""
    message: "str"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipAccountDetailError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["error"] = value["error"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetMembershipAccountDetailError:
    out: GetMembershipAccountDetailError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "GetMembershipAccountDetailError.account_id required"
        )
    if "error" in data:
        out["error"] = data["error"]
    else:
        raise DeserializationError("GetMembershipAccountDetailError.error required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("GetMembershipAccountDetailError.message required")
    return out
