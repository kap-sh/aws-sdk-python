"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long_min1
    import aws_sdk_kafkaconnect.types.__string


class WorkerConfiguration(TypedDict):
    revision: "aws_sdk_kafkaconnect.types.__long_min1.__longMin1"
    """<p>The revision of the worker configuration.</p>"""
    worker_configuration_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfiguration) -> dict:
    out: dict = {}
    out["revision"] = value.get("revision", 0)
    out["workerConfigurationArn"] = value["worker_configuration_arn"]
    return out


def deserialize_json(data: dict) -> WorkerConfiguration:
    out: WorkerConfiguration = {}  # type: ignore[typeddict-item]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if "workerConfigurationArn" in data:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    else:
        raise DeserializationError(
            "WorkerConfiguration.worker_configuration_arn required"
        )
    return out
