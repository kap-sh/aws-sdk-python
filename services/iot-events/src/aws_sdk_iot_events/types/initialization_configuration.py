"""Generated from Smithy shape ``com.amazonaws.iotevents#InitializationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.disabled_on_initialization


class InitializationConfiguration(TypedDict):
    disabled_on_initialization: (
        "aws_sdk_iot_events.types.disabled_on_initialization.DisabledOnInitialization"
    )
    """<p>The value must be <code>TRUE</code> or <code>FALSE</code>. If <code>FALSE</code>, all alarm instances created based on the alarm model are activated. The default value is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitializationConfiguration) -> dict:
    out: dict = {}
    out["disabledOnInitialization"] = value["disabled_on_initialization"]
    return out


def deserialize_json(data: dict) -> InitializationConfiguration:
    out: InitializationConfiguration = {}  # type: ignore[typeddict-item]
    if "disabledOnInitialization" in data:
        out["disabled_on_initialization"] = data["disabledOnInitialization"]
    else:
        raise DeserializationError(
            "InitializationConfiguration.disabled_on_initialization required"
        )
    return out
