"""Generated from Smithy shape ``com.amazonaws.securityir#BatchGetMemberAccountDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.aws_account_ids
    import aws_sdk_security_ir.types.membership_id


class BatchGetMemberAccountDetailsRequest(TypedDict, closed=True):
    membership_id: "aws_sdk_security_ir.types.membership_id.MembershipId"
    """<p>Required element used in combination with BatchGetMemberAccountDetails to identify the membership ID to query. </p>"""
    account_ids: "aws_sdk_security_ir.types.aws_account_ids.AWSAccountIds"
    """<p>Optional element to query the membership relationship status to a provided list of account IDs.</p> <note> <p> AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be <code>123123123</code> which is nine digits, and with zero-prepend would be <code>000123123123</code>. Not zero-prepending to 12 digits could result in errors. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMemberAccountDetailsRequest) -> dict:
    out: dict = {}
    import aws_sdk_security_ir.types.aws_account_ids

    out["accountIds"] = aws_sdk_security_ir.types.aws_account_ids.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetMemberAccountDetailsRequest:
    out: BatchGetMemberAccountDetailsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_security_ir.types.aws_account_ids

        out["account_ids"] = aws_sdk_security_ir.types.aws_account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        raise DeserializationError(
            "BatchGetMemberAccountDetailsRequest.account_ids required"
        )
    return out
