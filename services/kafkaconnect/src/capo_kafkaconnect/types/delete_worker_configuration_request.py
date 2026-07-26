"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteWorkerConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class DeleteWorkerConfigurationRequest(TypedDict, closed=True):
    worker_configuration_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the worker configuration that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkerConfigurationRequest:
    out: DeleteWorkerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
