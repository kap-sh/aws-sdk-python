"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryScanningConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.repository_scanning_configuration

RepositoryScanningConfigurationList: TypeAlias = list[
    "capo_ecr.types.repository_scanning_configuration.RepositoryScanningConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryScanningConfigurationList) -> list:
    import capo_ecr.types.repository_scanning_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.repository_scanning_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryScanningConfigurationList:
    import capo_ecr.types.repository_scanning_configuration

    out: RepositoryScanningConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecr.types.repository_scanning_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
