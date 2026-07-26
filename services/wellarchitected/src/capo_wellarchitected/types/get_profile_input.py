"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_version


class GetProfileInput(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    profile_version: NotRequired[
        "capo_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The profile version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileInput:
    out: GetProfileInput = {}  # type: ignore[typeddict-item]
    return out
