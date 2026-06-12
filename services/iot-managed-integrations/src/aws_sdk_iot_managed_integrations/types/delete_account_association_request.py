"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteAccountAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_id


class DeleteAccountAssociationRequest(TypedDict):
    account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the account association to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountAssociationRequest:
    out: DeleteAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
