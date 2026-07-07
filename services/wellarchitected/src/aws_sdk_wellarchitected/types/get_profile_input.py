"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_version


class GetProfileInput(TypedDict, closed=True):
    profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    profile_version: NotRequired[
        "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The profile version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileInput:
    out: GetProfileInput = {}  # type: ignore[typeddict-item]
    return out
