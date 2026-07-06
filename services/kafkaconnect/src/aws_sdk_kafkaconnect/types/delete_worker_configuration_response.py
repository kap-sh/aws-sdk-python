"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteWorkerConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.worker_configuration_state


class DeleteWorkerConfigurationResponse(TypedDict, closed=True):
    worker_configuration_arn: NotRequired[
        "aws_sdk_kafkaconnect.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the worker configuration that you requested to delete.</p>"""
    worker_configuration_state: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_state.WorkerConfigurationState"
    ]
    """<p>The state of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkerConfigurationResponse) -> dict:
    out: dict = {}
    if "worker_configuration_arn" in value:
        out["workerConfigurationArn"] = value["worker_configuration_arn"]
    if "worker_configuration_state" in value:
        out["workerConfigurationState"] = value["worker_configuration_state"]
    return out


def deserialize_json(data: dict) -> DeleteWorkerConfigurationResponse:
    out: DeleteWorkerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "workerConfigurationArn" in data:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    if "workerConfigurationState" in data:
        out["worker_configuration_state"] = data["workerConfigurationState"]
    return out
