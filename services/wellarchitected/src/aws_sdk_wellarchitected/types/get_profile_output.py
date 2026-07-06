"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile


class GetProfileOutput(TypedDict, closed=True):
    profile: NotRequired["aws_sdk_wellarchitected.types.profile.Profile"]
    """<p>The profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileOutput) -> dict:
    out: dict = {}
    if "profile" in value:
        import aws_sdk_wellarchitected.types.profile

        out["Profile"] = aws_sdk_wellarchitected.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> GetProfileOutput:
    out: GetProfileOutput = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        import aws_sdk_wellarchitected.types.profile

        out["profile"] = aws_sdk_wellarchitected.types.profile.deserialize_json(
            data["Profile"]
        )
    return out
