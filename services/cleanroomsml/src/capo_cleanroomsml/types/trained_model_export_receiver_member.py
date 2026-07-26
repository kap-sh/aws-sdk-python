"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportReceiverMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id


class TrainedModelExportReceiverMember(TypedDict, closed=True):
    account_id: "capo_cleanroomsml.types.account_id.AccountId"
    """<p>The account ID of the member who will receive trained model exports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportReceiverMember) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> TrainedModelExportReceiverMember:
    out: TrainedModelExportReceiverMember = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "TrainedModelExportReceiverMember.account_id required"
        )
    return out
