"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingModeResourceTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.resource_type

RecordingModeResourceTypesList: TypeAlias = list[
    "capo_config_service.types.resource_type.ResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingModeResourceTypesList) -> list:
    import capo_config_service.types.resource_type

    out: list = []
    for item in value:
        out.append(capo_config_service.types.resource_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecordingModeResourceTypesList:
    import capo_config_service.types.resource_type

    out: RecordingModeResourceTypesList = []
    for item in data:
        out.append(
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(item)
        )
    return out
