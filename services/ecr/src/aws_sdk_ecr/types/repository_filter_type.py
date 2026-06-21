"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

RepositoryFilterType: TypeAlias = Literal["PREFIX_MATCH",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryFilterType:
    return cast(RepositoryFilterType, data)
