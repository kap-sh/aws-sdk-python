"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.random_cut_forest_configuration


class _AnomalyDetectorConfiguration_randomCutForest(TypedDict, closed=True):
    randomCutForest: (
        "aws_sdk_amp.types.random_cut_forest_configuration.RandomCutForestConfiguration"
    )


AnomalyDetectorConfiguration: TypeAlias = _AnomalyDetectorConfiguration_randomCutForest


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorConfiguration) -> dict:
    if "randomCutForest" in value:
        import aws_sdk_amp.types.random_cut_forest_configuration

        return {
            "randomCutForest": aws_sdk_amp.types.random_cut_forest_configuration.serialize_json(
                value["randomCutForest"]
            )
        }
    else:
        raise SerializationError("AnomalyDetectorConfiguration: no variant present")


def deserialize_json(data: dict) -> AnomalyDetectorConfiguration:
    if "randomCutForest" in data:
        import aws_sdk_amp.types.random_cut_forest_configuration

        return {
            "randomCutForest": aws_sdk_amp.types.random_cut_forest_configuration.deserialize_json(
                data["randomCutForest"]
            )
        }
    else:
        raise DeserializationError(
            "AnomalyDetectorConfiguration: no recognized variant key"
        )
