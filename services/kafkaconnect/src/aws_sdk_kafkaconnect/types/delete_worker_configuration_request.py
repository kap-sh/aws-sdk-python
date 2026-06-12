"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteWorkerConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DeleteWorkerConfigurationRequest(TypedDict):
    worker_configuration_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the worker configuration that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkerConfigurationRequest:
    out: DeleteWorkerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
