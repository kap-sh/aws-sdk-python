"""Generated from Smithy shape ``com.amazonaws.securityir#GetMembershipAccountDetailErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.get_membership_account_detail_error

GetMembershipAccountDetailErrors: TypeAlias = list[
    "capo_security_ir.types.get_membership_account_detail_error.GetMembershipAccountDetailError"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipAccountDetailErrors) -> list:
    import capo_security_ir.types.get_membership_account_detail_error

    out: list = []
    for item in value:
        out.append(
            capo_security_ir.types.get_membership_account_detail_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetMembershipAccountDetailErrors:
    import capo_security_ir.types.get_membership_account_detail_error

    out: GetMembershipAccountDetailErrors = []
    for item in data:
        out.append(
            capo_security_ir.types.get_membership_account_detail_error.deserialize_json(
                item
            )
        )
    return out
