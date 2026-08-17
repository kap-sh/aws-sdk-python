"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryScanningConfigurationFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.repository_scanning_configuration_failure

RepositoryScanningConfigurationFailureList: TypeAlias = list[
    "capo_ecr.types.repository_scanning_configuration_failure.RepositoryScanningConfigurationFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryScanningConfigurationFailureList) -> list:
    import capo_ecr.types.repository_scanning_configuration_failure

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.repository_scanning_configuration_failure.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryScanningConfigurationFailureList:
    import capo_ecr.types.repository_scanning_configuration_failure

    out: RepositoryScanningConfigurationFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecr.types.repository_scanning_configuration_failure.deserialize_aws_json_1_1(
                item
            )
        )
    return out
