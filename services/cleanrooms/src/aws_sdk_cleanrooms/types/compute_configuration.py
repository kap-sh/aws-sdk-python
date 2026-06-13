"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.worker_compute_configuration


class _ComputeConfiguration_worker(TypedDict):
    worker: "aws_sdk_cleanrooms.types.worker_compute_configuration.WorkerComputeConfiguration"


ComputeConfiguration: TypeAlias = _ComputeConfiguration_worker


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfiguration) -> dict:
    if "worker" in value:
        import aws_sdk_cleanrooms.types.worker_compute_configuration

        return {
            "worker": aws_sdk_cleanrooms.types.worker_compute_configuration.serialize_json(
                value["worker"]
            )
        }
    else:
        raise SerializationError("ComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ComputeConfiguration:
    if "worker" in data:
        import aws_sdk_cleanrooms.types.worker_compute_configuration

        return {
            "worker": aws_sdk_cleanrooms.types.worker_compute_configuration.deserialize_json(
                data["worker"]
            )
        }
    else:
        raise DeserializationError("ComputeConfiguration: no recognized variant key")
