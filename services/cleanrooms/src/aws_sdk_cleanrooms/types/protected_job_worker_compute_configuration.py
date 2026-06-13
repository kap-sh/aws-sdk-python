"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobWorkerComputeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_worker_compute_type
    import aws_sdk_cleanrooms.types.worker_compute_configuration_properties


class ProtectedJobWorkerComputeConfiguration(TypedDict):
    type: "aws_sdk_cleanrooms.types.protected_job_worker_compute_type.ProtectedJobWorkerComputeType"
    """<p>The worker compute configuration type.</p>"""
    number: "int"
    """<p>The number of workers for a PySpark job.</p>"""
    properties: NotRequired[
        "aws_sdk_cleanrooms.types.worker_compute_configuration_properties.WorkerComputeConfigurationProperties"
    ]
    """<p>The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your Clean Rooms workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobWorkerComputeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job_worker_compute_type

    out["type"] = (
        aws_sdk_cleanrooms.types.protected_job_worker_compute_type.serialize_json(
            value["type"]
        )
    )
    out["number"] = value["number"]
    if "properties" in value:
        import aws_sdk_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            aws_sdk_cleanrooms.types.worker_compute_configuration_properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedJobWorkerComputeConfiguration:
    out: ProtectedJobWorkerComputeConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.protected_job_worker_compute_type

        out["type"] = (
            aws_sdk_cleanrooms.types.protected_job_worker_compute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedJobWorkerComputeConfiguration.type required"
        )
    if "number" in data:
        out["number"] = data["number"]
    else:
        raise DeserializationError(
            "ProtectedJobWorkerComputeConfiguration.number required"
        )
    if "properties" in data:
        import aws_sdk_cleanrooms.types.worker_compute_configuration_properties

        out["properties"] = (
            aws_sdk_cleanrooms.types.worker_compute_configuration_properties.deserialize_json(
                data["properties"]
            )
        )
    return out
