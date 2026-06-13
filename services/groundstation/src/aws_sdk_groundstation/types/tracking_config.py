"""Generated from Smithy shape ``com.amazonaws.groundstation#TrackingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.criticality


class TrackingConfig(TypedDict):
    autotrack: "aws_sdk_groundstation.types.criticality.Criticality"
    """<p>Current setting for autotrack.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingConfig) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.criticality

    out["autotrack"] = aws_sdk_groundstation.types.criticality.serialize_json(
        value["autotrack"]
    )
    return out


def deserialize_json(data: dict) -> TrackingConfig:
    out: TrackingConfig = {}  # type: ignore[typeddict-item]
    if "autotrack" in data:
        import aws_sdk_groundstation.types.criticality

        out["autotrack"] = aws_sdk_groundstation.types.criticality.deserialize_json(
            data["autotrack"]
        )
    else:
        raise DeserializationError("TrackingConfig.autotrack required")
    return out
