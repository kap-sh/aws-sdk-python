"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PayerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id


class PayerConfiguration(TypedDict, closed=True):
    compute_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying compute costs.</p>"""
    synthetic_data_payer_account_id: NotRequired[
        "capo_cleanroomsml.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that is responsible for paying synthetic data generation costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PayerConfiguration) -> dict:
    out: dict = {}
    if "compute_payer_account_id" in value:
        out["computePayerAccountId"] = value["compute_payer_account_id"]
    if "synthetic_data_payer_account_id" in value:
        out["syntheticDataPayerAccountId"] = value["synthetic_data_payer_account_id"]
    return out


def deserialize_json(data: dict) -> PayerConfiguration:
    out: PayerConfiguration = {}  # type: ignore[typeddict-item]
    if "computePayerAccountId" in data:
        out["compute_payer_account_id"] = data["computePayerAccountId"]
    if "syntheticDataPayerAccountId" in data:
        out["synthetic_data_payer_account_id"] = data["syntheticDataPayerAccountId"]
    return out
