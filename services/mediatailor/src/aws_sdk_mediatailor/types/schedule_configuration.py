"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.clip_range
    import aws_sdk_mediatailor.types.transition


class ScheduleConfiguration(TypedDict):
    transition: "aws_sdk_mediatailor.types.transition.Transition"
    """<p>Program transition configurations.</p>"""
    clip_range: NotRequired["aws_sdk_mediatailor.types.clip_range.ClipRange"]
    """<p>Program clip range configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.transition

    out["Transition"] = aws_sdk_mediatailor.types.transition.serialize_json(
        value["transition"]
    )
    if "clip_range" in value:
        import aws_sdk_mediatailor.types.clip_range

        out["ClipRange"] = aws_sdk_mediatailor.types.clip_range.serialize_json(
            value["clip_range"]
        )
    return out


def deserialize_json(data: dict) -> ScheduleConfiguration:
    out: ScheduleConfiguration = {}  # type: ignore[typeddict-item]
    if "Transition" in data:
        import aws_sdk_mediatailor.types.transition

        out["transition"] = aws_sdk_mediatailor.types.transition.deserialize_json(
            data["Transition"]
        )
    else:
        raise DeserializationError("ScheduleConfiguration.transition required")
    if "ClipRange" in data:
        import aws_sdk_mediatailor.types.clip_range

        out["clip_range"] = aws_sdk_mediatailor.types.clip_range.deserialize_json(
            data["ClipRange"]
        )
    return out
