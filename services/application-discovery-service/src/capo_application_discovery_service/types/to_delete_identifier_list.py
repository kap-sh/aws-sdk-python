"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ToDeleteIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.import_task_identifier

ToDeleteIdentifierList: TypeAlias = list[
    "capo_application_discovery_service.types.import_task_identifier.ImportTaskIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToDeleteIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ToDeleteIdentifierList:
    return list(data)
