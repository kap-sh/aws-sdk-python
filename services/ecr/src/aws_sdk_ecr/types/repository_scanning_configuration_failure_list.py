"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryScanningConfigurationFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.repository_scanning_configuration_failure

RepositoryScanningConfigurationFailureList: TypeAlias = list[
    "aws_sdk_ecr.types.repository_scanning_configuration_failure.RepositoryScanningConfigurationFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryScanningConfigurationFailureList) -> list:
    import aws_sdk_ecr.types.repository_scanning_configuration_failure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.repository_scanning_configuration_failure.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryScanningConfigurationFailureList:
    import aws_sdk_ecr.types.repository_scanning_configuration_failure

    out: RepositoryScanningConfigurationFailureList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.repository_scanning_configuration_failure.deserialize_aws_json_1_1(
                item
            )
        )
    return out
