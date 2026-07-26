"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_networkflowmonitor.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.account_id


class _TargetId_accountId(TypedDict, closed=True):
    accountId: "capo_networkflowmonitor.types.account_id.AccountId"


TargetId: TypeAlias = _TargetId_accountId


# --- restJson1 ser/de ---
def serialize_json(value: TargetId) -> dict:
    if "accountId" in value:
        return {"accountId": value["accountId"]}
    else:
        raise SerializationError("TargetId: no variant present")


def deserialize_json(data: dict) -> TargetId:
    if "accountId" in data:
        return {"accountId": data["accountId"]}
    else:
        raise DeserializationError("TargetId: no recognized variant key")
