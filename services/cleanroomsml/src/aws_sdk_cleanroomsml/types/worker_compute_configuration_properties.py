"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#WorkerComputeConfigurationProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.spark_properties


class _WorkerComputeConfigurationProperties_spark(TypedDict, closed=True):
    spark: "aws_sdk_cleanroomsml.types.spark_properties.SparkProperties"


WorkerComputeConfigurationProperties: TypeAlias = (
    _WorkerComputeConfigurationProperties_spark
)


# --- restJson1 ser/de ---
def serialize_json(value: WorkerComputeConfigurationProperties) -> dict:
    if "spark" in value:
        import aws_sdk_cleanroomsml.types.spark_properties

        return {
            "spark": aws_sdk_cleanroomsml.types.spark_properties.serialize_json(
                value["spark"]
            )
        }
    else:
        raise SerializationError(
            "WorkerComputeConfigurationProperties: no variant present"
        )


def deserialize_json(data: dict) -> WorkerComputeConfigurationProperties:
    if "spark" in data:
        import aws_sdk_cleanroomsml.types.spark_properties

        return {
            "spark": aws_sdk_cleanroomsml.types.spark_properties.deserialize_json(
                data["spark"]
            )
        }
    else:
        raise DeserializationError(
            "WorkerComputeConfigurationProperties: no recognized variant key"
        )
