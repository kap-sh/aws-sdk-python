"""Generated from Smithy shape ``com.amazonaws.inspector2#EnableDelegatedAdminAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.client_token


class EnableDelegatedAdminAccountRequest(TypedDict):
    delegated_admin_account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator.</p>"""
    client_token: NotRequired["aws_sdk_inspector2.types.client_token.ClientToken"]
    """<p>The idempotency token for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDelegatedAdminAccountRequest) -> dict:
    out: dict = {}
    out["delegatedAdminAccountId"] = value["delegated_admin_account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> EnableDelegatedAdminAccountRequest:
    out: EnableDelegatedAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "delegatedAdminAccountId" in data:
        out["delegated_admin_account_id"] = data["delegatedAdminAccountId"]
    else:
        raise DeserializationError(
            "EnableDelegatedAdminAccountRequest.delegated_admin_account_id required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
