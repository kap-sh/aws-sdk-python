"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__string


class WorkerConfigurationDescription(TypedDict, closed=True):
    revision: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The revision of the worker configuration.</p>"""
    worker_configuration_arn: NotRequired[
        "aws_sdk_kafkaconnect.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationDescription) -> dict:
    out: dict = {}
    out["revision"] = value.get("revision", 0)
    if "worker_configuration_arn" in value:
        out["workerConfigurationArn"] = value["worker_configuration_arn"]
    return out


def deserialize_json(data: dict) -> WorkerConfigurationDescription:
    out: WorkerConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if "workerConfigurationArn" in data:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    return out
