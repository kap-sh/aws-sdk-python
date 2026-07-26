"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterpolatedAssetPropertyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.variant


class InterpolatedAssetPropertyValue(TypedDict, closed=True):
    timestamp: "capo_iotsitewise.types.time_in_nanos.TimeInNanos"
    value: "capo_iotsitewise.types.variant.Variant"


# --- restJson1 ser/de ---
def serialize_json(value: InterpolatedAssetPropertyValue) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.time_in_nanos

    out["timestamp"] = capo_iotsitewise.types.time_in_nanos.serialize_json(
        value["timestamp"]
    )
    import capo_iotsitewise.types.variant

    out["value"] = capo_iotsitewise.types.variant.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> InterpolatedAssetPropertyValue:
    out: InterpolatedAssetPropertyValue = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import capo_iotsitewise.types.time_in_nanos

        out["timestamp"] = capo_iotsitewise.types.time_in_nanos.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("InterpolatedAssetPropertyValue.timestamp required")
    if "value" in data:
        import capo_iotsitewise.types.variant

        out["value"] = capo_iotsitewise.types.variant.deserialize_json(data["value"])
    else:
        raise DeserializationError("InterpolatedAssetPropertyValue.value required")
    return out
