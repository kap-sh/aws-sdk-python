"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#__listOfWorkerConfigurationSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafkaconnect.types.worker_configuration_summary

__listOfWorkerConfigurationSummary: TypeAlias = list[
    "capo_kafkaconnect.types.worker_configuration_summary.WorkerConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfWorkerConfigurationSummary) -> list:
    import capo_kafkaconnect.types.worker_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_kafkaconnect.types.worker_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfWorkerConfigurationSummary:
    import capo_kafkaconnect.types.worker_configuration_summary

    out: __listOfWorkerConfigurationSummary = []
    for item in data:
        out.append(
            capo_kafkaconnect.types.worker_configuration_summary.deserialize_json(item)
        )
    return out
