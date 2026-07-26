"""Generated from Smithy shape ``com.amazonaws.securityir#BatchGetMemberAccountDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.get_membership_account_detail_errors
    import capo_security_ir.types.get_membership_account_detail_items


class BatchGetMemberAccountDetailsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_security_ir.types.get_membership_account_detail_items.GetMembershipAccountDetailItems"
    ]
    """<p>The response element providing responses for requests to GetMembershipAccountDetails.</p>"""
    errors: NotRequired[
        "capo_security_ir.types.get_membership_account_detail_errors.GetMembershipAccountDetailErrors"
    ]
    """<p>The response element providing error messages for requests to GetMembershipAccountDetails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMemberAccountDetailsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_security_ir.types.get_membership_account_detail_items

        out["items"] = (
            capo_security_ir.types.get_membership_account_detail_items.serialize_json(
                value["items"]
            )
        )
    if "errors" in value:
        import capo_security_ir.types.get_membership_account_detail_errors

        out["errors"] = (
            capo_security_ir.types.get_membership_account_detail_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetMemberAccountDetailsResponse:
    out: BatchGetMemberAccountDetailsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_security_ir.types.get_membership_account_detail_items

        out["items"] = (
            capo_security_ir.types.get_membership_account_detail_items.deserialize_json(
                data["items"]
            )
        )
    if "errors" in data:
        import capo_security_ir.types.get_membership_account_detail_errors

        out["errors"] = (
            capo_security_ir.types.get_membership_account_detail_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
