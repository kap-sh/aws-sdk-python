"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeWorkerConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DescribeWorkerConfigurationRequest(TypedDict):
    worker_configuration_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the worker configuration that you want to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkerConfigurationRequest:
    out: DescribeWorkerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
