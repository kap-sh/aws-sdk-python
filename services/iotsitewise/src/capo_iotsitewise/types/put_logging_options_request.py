"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutLoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.logging_options


class PutLoggingOptionsRequest(TypedDict, closed=True):
    logging_options: "capo_iotsitewise.types.logging_options.LoggingOptions"
    """<p>The logging options to set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLoggingOptionsRequest) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.logging_options

    out["loggingOptions"] = capo_iotsitewise.types.logging_options.serialize_json(
        value["logging_options"]
    )
    return out


def deserialize_json(data: dict) -> PutLoggingOptionsRequest:
    out: PutLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "loggingOptions" in data:
        import capo_iotsitewise.types.logging_options

        out["logging_options"] = (
            capo_iotsitewise.types.logging_options.deserialize_json(
                data["loggingOptions"]
            )
        )
    else:
        raise DeserializationError("PutLoggingOptionsRequest.logging_options required")
    return out
