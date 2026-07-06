"""Generated from Smithy shape ``com.amazonaws.auditmanager#RegisterOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id


class RegisterOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: "aws_sdk_auditmanager.types.account_id.AccountId"
    """<p> The identifier for the delegated administrator account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    out["adminAccountId"] = value["admin_account_id"]
    return out


def deserialize_json(data: dict) -> RegisterOrganizationAdminAccountRequest:
    out: RegisterOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    else:
        raise DeserializationError(
            "RegisterOrganizationAdminAccountRequest.admin_account_id required"
        )
    return out
