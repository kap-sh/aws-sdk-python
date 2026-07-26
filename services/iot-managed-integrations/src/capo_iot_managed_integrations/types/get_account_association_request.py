"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetAccountAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id


class GetAccountAssociationRequest(TypedDict, closed=True):
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the account association to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountAssociationRequest:
    out: GetAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
