"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateProgramScheduleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.clip_range
    import aws_sdk_mediatailor.types.update_program_transition


class UpdateProgramScheduleConfiguration(TypedDict):
    transition: NotRequired[
        "aws_sdk_mediatailor.types.update_program_transition.UpdateProgramTransition"
    ]
    """<p>Program transition configuration.</p>"""
    clip_range: NotRequired["aws_sdk_mediatailor.types.clip_range.ClipRange"]
    """<p>Program clip range configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProgramScheduleConfiguration) -> dict:
    out: dict = {}
    if "transition" in value:
        import aws_sdk_mediatailor.types.update_program_transition

        out["Transition"] = (
            aws_sdk_mediatailor.types.update_program_transition.serialize_json(
                value["transition"]
            )
        )
    if "clip_range" in value:
        import aws_sdk_mediatailor.types.clip_range

        out["ClipRange"] = aws_sdk_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProgramScheduleConfiguration:
    out: UpdateProgramScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "Transition" in data:
        import aws_sdk_mediatailor.types.update_program_transition

        out["transition"] = (
            aws_sdk_mediatailor.types.update_program_transition.deserialize_json(
                data["Transition"]
            )
        )
    if "ClipRange" in data:
        import aws_sdk_mediatailor.types.clip_range

        out["clip_range"] = aws_sdk_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    return out
