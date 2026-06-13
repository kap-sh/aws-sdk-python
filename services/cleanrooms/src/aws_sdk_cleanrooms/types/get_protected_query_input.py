"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetProtectedQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_query_identifier


class GetProtectedQueryInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership in a protected query instance.</p>"""
    protected_query_identifier: (
        "aws_sdk_cleanrooms.types.protected_query_identifier.ProtectedQueryIdentifier"
    )
    """<p>The identifier for a protected query instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProtectedQueryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProtectedQueryInput:
    out: GetProtectedQueryInput = {}  # type: ignore[typeddict-item]
    return out
