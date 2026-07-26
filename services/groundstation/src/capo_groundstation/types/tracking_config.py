"""Generated from Smithy shape ``com.amazonaws.groundstation#TrackingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.criticality


class TrackingConfig(TypedDict, closed=True):
    autotrack: "capo_groundstation.types.criticality.Criticality"
    """<p>Current setting for autotrack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingConfig) -> dict:
    out: dict = {}
    import capo_groundstation.types.criticality

    out["autotrack"] = capo_groundstation.types.criticality.serialize_json(
        value["autotrack"]
    )
    return out


def deserialize_json(data: dict) -> TrackingConfig:
    out: TrackingConfig = {}  # type: ignore[typeddict-item]
    if "autotrack" in data:
        import capo_groundstation.types.criticality

        out["autotrack"] = capo_groundstation.types.criticality.deserialize_json(
            data["autotrack"]
        )
    else:
        raise DeserializationError("TrackingConfig.autotrack required")
    return out
