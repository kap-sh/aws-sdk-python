"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobMemberOutputConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id


class ProtectedJobMemberOutputConfigurationOutput(TypedDict, closed=True):
    account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p> The account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobMemberOutputConfigurationOutput) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJobMemberOutputConfigurationOutput:
    out: ProtectedJobMemberOutputConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "ProtectedJobMemberOutputConfigurationOutput.account_id required"
        )
    return out
