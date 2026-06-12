"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfWorkerConfigurationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.worker_configuration_summary

__listOfWorkerConfigurationSummary: TypeAlias = list[
    "aws_sdk_kafkaconnect.types.worker_configuration_summary.WorkerConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfWorkerConfigurationSummary) -> list:
    import aws_sdk_kafkaconnect.types.worker_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kafkaconnect.types.worker_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfWorkerConfigurationSummary:
    import aws_sdk_kafkaconnect.types.worker_configuration_summary

    out: __listOfWorkerConfigurationSummary = []
    for item in data:
        out.append(
            aws_sdk_kafkaconnect.types.worker_configuration_summary.deserialize_json(
                item
            )
        )
    return out
