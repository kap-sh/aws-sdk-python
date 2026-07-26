"""Generated from Smithy shape ``com.amazonaws.iotsitewise#LoggingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.logging_level


class LoggingOptions(TypedDict, closed=True):
    level: "capo_iotsitewise.types.logging_level.LoggingLevel"
    """<p>The IoT SiteWise logging verbosity level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingOptions) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.logging_level

    out["level"] = capo_iotsitewise.types.logging_level.serialize_json(value["level"])
    return out


def deserialize_json(data: dict) -> LoggingOptions:
    out: LoggingOptions = {}  # type: ignore[typeddict-item]
    if "level" in data:
        import capo_iotsitewise.types.logging_level

        out["level"] = capo_iotsitewise.types.logging_level.deserialize_json(
            data["level"]
        )
    else:
        raise DeserializationError("LoggingOptions.level required")
    return out
