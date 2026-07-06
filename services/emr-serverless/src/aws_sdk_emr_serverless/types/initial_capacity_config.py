"""Generated from Smithy shape ``com.amazonaws.emrserverless#InitialCapacityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.worker_counts
    import aws_sdk_emr_serverless.types.worker_resource_config


class InitialCapacityConfig(TypedDict, closed=True):
    worker_count: "aws_sdk_emr_serverless.types.worker_counts.WorkerCounts"
    """<p>The number of workers in the initial capacity configuration.</p>"""
    worker_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.worker_resource_config.WorkerResourceConfig"
    ]
    """<p>The resource configuration of the initial capacity configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitialCapacityConfig) -> dict:
    out: dict = {}
    out["workerCount"] = value.get("worker_count", 0)
    if "worker_configuration" in value:
        import aws_sdk_emr_serverless.types.worker_resource_config

        out["workerConfiguration"] = (
            aws_sdk_emr_serverless.types.worker_resource_config.serialize_json(
                value["worker_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> InitialCapacityConfig:
    out: InitialCapacityConfig = {}  # type: ignore[typeddict-item]
    if "workerCount" in data:
        out["worker_count"] = data["workerCount"]
    else:
        out["worker_count"] = 0
    if "workerConfiguration" in data:
        import aws_sdk_emr_serverless.types.worker_resource_config

        out["worker_configuration"] = (
            aws_sdk_emr_serverless.types.worker_resource_config.deserialize_json(
                data["workerConfiguration"]
            )
        )
    return out
