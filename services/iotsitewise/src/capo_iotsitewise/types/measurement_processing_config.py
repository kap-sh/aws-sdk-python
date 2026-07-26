"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MeasurementProcessingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.forwarding_config


class MeasurementProcessingConfig(TypedDict, closed=True):
    forwarding_config: "capo_iotsitewise.types.forwarding_config.ForwardingConfig"
    """<p>The forwarding configuration for the given measurement property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeasurementProcessingConfig) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.forwarding_config

    out["forwardingConfig"] = capo_iotsitewise.types.forwarding_config.serialize_json(
        value["forwarding_config"]
    )
    return out


def deserialize_json(data: dict) -> MeasurementProcessingConfig:
    out: MeasurementProcessingConfig = {}  # type: ignore[typeddict-item]
    if "forwardingConfig" in data:
        import capo_iotsitewise.types.forwarding_config

        out["forwarding_config"] = (
            capo_iotsitewise.types.forwarding_config.deserialize_json(
                data["forwardingConfig"]
            )
        )
    else:
        raise DeserializationError(
            "MeasurementProcessingConfig.forwarding_config required"
        )
    return out
