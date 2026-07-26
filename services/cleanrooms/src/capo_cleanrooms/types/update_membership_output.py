"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateMembershipOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership


class UpdateMembershipOutput(TypedDict, closed=True):
    membership: "capo_cleanrooms.types.membership.Membership"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMembershipOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.membership

    out["membership"] = capo_cleanrooms.types.membership.serialize_json(
        value["membership"]
    )
    return out


def deserialize_json(data: dict) -> UpdateMembershipOutput:
    out: UpdateMembershipOutput = {}  # type: ignore[typeddict-item]
    if "membership" in data:
        import capo_cleanrooms.types.membership

        out["membership"] = capo_cleanrooms.types.membership.deserialize_json(
            data["membership"]
        )
    else:
        raise DeserializationError("UpdateMembershipOutput.membership required")
    return out
