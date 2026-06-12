"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.repository_filter

RepositoryFilterList: TypeAlias = list[
    "aws_sdk_ecr.types.repository_filter.RepositoryFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryFilterList) -> list:
    import aws_sdk_ecr.types.repository_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.repository_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryFilterList:
    import aws_sdk_ecr.types.repository_filter

    out: RepositoryFilterList = []
    for item in data:
        out.append(aws_sdk_ecr.types.repository_filter.deserialize_aws_json_1_1(item))
    return out
