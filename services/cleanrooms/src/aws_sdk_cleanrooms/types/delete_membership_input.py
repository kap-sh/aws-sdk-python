"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier


class DeleteMembershipInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMembershipInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMembershipInput:
    out: DeleteMembershipInput = {}  # type: ignore[typeddict-item]
    return out
