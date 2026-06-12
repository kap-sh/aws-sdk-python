"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ApplicationIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.application_id

ApplicationIdsList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.application_id.ApplicationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApplicationIdsList:
    return list(data)
