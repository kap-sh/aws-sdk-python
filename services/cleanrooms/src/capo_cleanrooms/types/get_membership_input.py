"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier


class GetMembershipInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembershipInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMembershipInput:
    out: GetMembershipInput = {}  # type: ignore[typeddict-item]
    return out
