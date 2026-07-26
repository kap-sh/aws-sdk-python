"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetMembershipOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership


class GetMembershipOutput(TypedDict, closed=True):
    membership: "capo_cleanrooms.types.membership.Membership"
    """<p>The membership retrieved for the provided identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.membership

    out["membership"] = capo_cleanrooms.types.membership.serialize_json(
        value["membership"]
    )
    return out


def deserialize_json(data: dict) -> GetMembershipOutput:
    out: GetMembershipOutput = {}  # type: ignore[typeddict-item]
    if "membership" in data:
        import capo_cleanrooms.types.membership

        out["membership"] = capo_cleanrooms.types.membership.deserialize_json(
            data["membership"]
        )
    else:
        raise DeserializationError("GetMembershipOutput.membership required")
    return out
