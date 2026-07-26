"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateProgramScheduleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.clip_range
    import capo_mediatailor.types.update_program_transition


class UpdateProgramScheduleConfiguration(TypedDict, closed=True):
    transition: NotRequired[
        "capo_mediatailor.types.update_program_transition.UpdateProgramTransition"
    ]
    """<p>Program transition configuration.</p>"""
    clip_range: NotRequired["capo_mediatailor.types.clip_range.ClipRange"]
    """<p>Program clip range configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProgramScheduleConfiguration) -> dict:
    out: dict = {}
    if "transition" in value:
        import capo_mediatailor.types.update_program_transition

        out["Transition"] = (
            capo_mediatailor.types.update_program_transition.serialize_json(
                value["transition"]
            )
        )
    if "clip_range" in value:
        import capo_mediatailor.types.clip_range

        out["ClipRange"] = capo_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProgramScheduleConfiguration:
    out: UpdateProgramScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "Transition" in data:
        import capo_mediatailor.types.update_program_transition

        out["transition"] = (
            capo_mediatailor.types.update_program_transition.deserialize_json(
                data["Transition"]
            )
        )
    if "ClipRange" in data:
        import capo_mediatailor.types.clip_range

        out["clip_range"] = capo_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    return out
