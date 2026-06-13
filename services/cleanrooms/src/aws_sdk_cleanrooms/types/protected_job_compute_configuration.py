"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration


class _ProtectedJobComputeConfiguration_worker(TypedDict):
    worker: "aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration.ProtectedJobWorkerComputeConfiguration"


ProtectedJobComputeConfiguration: TypeAlias = _ProtectedJobComputeConfiguration_worker


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobComputeConfiguration) -> dict:
    if "worker" in value:
        import aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration

        return {
            "worker": aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration.serialize_json(
                value["worker"]
            )
        }
    else:
        raise SerializationError("ProtectedJobComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ProtectedJobComputeConfiguration:
    if "worker" in data:
        import aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration

        return {
            "worker": aws_sdk_cleanrooms.types.protected_job_worker_compute_configuration.deserialize_json(
                data["worker"]
            )
        }
    else:
        raise DeserializationError(
            "ProtectedJobComputeConfiguration: no recognized variant key"
        )
