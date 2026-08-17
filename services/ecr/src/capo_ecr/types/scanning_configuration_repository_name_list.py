"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningConfigurationRepositoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.repository_name

ScanningConfigurationRepositoryNameList: TypeAlias = list[
    "capo_ecr.types.repository_name.RepositoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningConfigurationRepositoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ScanningConfigurationRepositoryNameList:
    return [item for item in data if item is not None]
