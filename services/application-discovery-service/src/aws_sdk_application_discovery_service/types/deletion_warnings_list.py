"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeletionWarningsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.deletion_warning

DeletionWarningsList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.deletion_warning.DeletionWarning"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletionWarningsList) -> list:
    import aws_sdk_application_discovery_service.types.deletion_warning

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.deletion_warning.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeletionWarningsList:
    import aws_sdk_application_discovery_service.types.deletion_warning

    out: DeletionWarningsList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.deletion_warning.deserialize_aws_json_1_1(
                item
            )
        )
    return out
