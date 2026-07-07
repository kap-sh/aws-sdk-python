"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricsConfigurationPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.noise_level_type


class MetricsConfigurationPolicy(TypedDict, closed=True):
    noise_level: "aws_sdk_cleanroomsml.types.noise_level_type.NoiseLevelType"
    """<p>The noise level for the generated metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsConfigurationPolicy) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.noise_level_type

    out["noiseLevel"] = aws_sdk_cleanroomsml.types.noise_level_type.serialize_json(
        value["noise_level"]
    )
    return out


def deserialize_json(data: dict) -> MetricsConfigurationPolicy:
    out: MetricsConfigurationPolicy = {}  # type: ignore[typeddict-item]
    if "noiseLevel" in data:
        import aws_sdk_cleanroomsml.types.noise_level_type

        out["noise_level"] = (
            aws_sdk_cleanroomsml.types.noise_level_type.deserialize_json(
                data["noiseLevel"]
            )
        )
    else:
        raise DeserializationError("MetricsConfigurationPolicy.noise_level required")
    return out
