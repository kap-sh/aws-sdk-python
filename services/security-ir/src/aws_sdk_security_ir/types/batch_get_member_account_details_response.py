"""Generated from Smithy shape ``com.amazonaws.securityir#BatchGetMemberAccountDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_security_ir.types.get_membership_account_detail_errors
    import aws_sdk_security_ir.types.get_membership_account_detail_items

class BatchGetMemberAccountDetailsResponse(TypedDict):
    items: NotRequired["aws_sdk_security_ir.types.get_membership_account_detail_items.GetMembershipAccountDetailItems"]
    """<p>The response element providing responses for requests to GetMembershipAccountDetails.</p>"""
    errors: NotRequired["aws_sdk_security_ir.types.get_membership_account_detail_errors.GetMembershipAccountDetailErrors"]
    """<p>The response element providing error messages for requests to GetMembershipAccountDetails.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMemberAccountDetailsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_security_ir.types.get_membership_account_detail_items
        out["items"] = aws_sdk_security_ir.types.get_membership_account_detail_items.serialize_json(value["items"])
    if "errors" in value:
        import aws_sdk_security_ir.types.get_membership_account_detail_errors
        out["errors"] = aws_sdk_security_ir.types.get_membership_account_detail_errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetMemberAccountDetailsResponse:
    out: BatchGetMemberAccountDetailsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_security_ir.types.get_membership_account_detail_items
        out["items"] = aws_sdk_security_ir.types.get_membership_account_detail_items.deserialize_json(data["items"])
    if "errors" in data:
        import aws_sdk_security_ir.types.get_membership_account_detail_errors
        out["errors"] = aws_sdk_security_ir.types.get_membership_account_detail_errors.deserialize_json(data["errors"])
    return out