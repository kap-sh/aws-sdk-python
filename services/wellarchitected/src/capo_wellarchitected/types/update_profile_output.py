"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateProfileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile


class UpdateProfileOutput(TypedDict, closed=True):
    profile: NotRequired["capo_wellarchitected.types.profile.Profile"]
    """<p>The profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileOutput) -> dict:
    out: dict = {}
    if "profile" in value:
        import capo_wellarchitected.types.profile

        out["Profile"] = capo_wellarchitected.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProfileOutput:
    out: UpdateProfileOutput = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        import capo_wellarchitected.types.profile

        out["profile"] = capo_wellarchitected.types.profile.deserialize_json(
            data["Profile"]
        )
    return out
