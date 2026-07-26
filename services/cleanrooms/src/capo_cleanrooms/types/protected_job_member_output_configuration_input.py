"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobMemberOutputConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id


class ProtectedJobMemberOutputConfigurationInput(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p> The account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobMemberOutputConfigurationInput) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJobMemberOutputConfigurationInput:
    out: ProtectedJobMemberOutputConfigurationInput = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "ProtectedJobMemberOutputConfigurationInput.account_id required"
        )
    return out
