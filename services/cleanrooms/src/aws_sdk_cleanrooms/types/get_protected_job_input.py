"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetProtectedJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_job_identifier


class GetProtectedJobInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> The identifier for a membership in a protected job instance.</p>"""
    protected_job_identifier: (
        "aws_sdk_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier"
    )
    """<p> The identifier for the protected job instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProtectedJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProtectedJobInput:
    out: GetProtectedJobInput = {}  # type: ignore[typeddict-item]
    return out
