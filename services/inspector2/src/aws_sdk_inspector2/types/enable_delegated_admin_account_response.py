"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableDelegatedAdminAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id


class EnableDelegatedAdminAccountResponse(TypedDict):
    delegated_admin_account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the successfully Amazon Inspector delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDelegatedAdminAccountResponse) -> dict:
    out: dict = {}
    out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    return out


def deserialize_json(data: dict) -> EnableDelegatedAdminAccountResponse:
    out: EnableDelegatedAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "delegatedAdminAccountId" in data:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    else:
        raise DeserializationError(
            "EnableDelegatedAdminAccountResponse.delegated_admin_account_id required"
        )
    return out
