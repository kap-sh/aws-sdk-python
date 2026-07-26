"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.repository_filter

RepositoryFilterList: TypeAlias = list[
    "capo_ecr.types.repository_filter.RepositoryFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryFilterList) -> list:
    import capo_ecr.types.repository_filter

    out: list = []
    for item in value:
        out.append(capo_ecr.types.repository_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryFilterList:
    import capo_ecr.types.repository_filter

    out: RepositoryFilterList = []
    for item in data:
        out.append(capo_ecr.types.repository_filter.deserialize_aws_json_1_1(item))
    return out
