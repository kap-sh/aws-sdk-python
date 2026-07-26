"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningRepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

ScanningRepositoryFilterType: TypeAlias = Literal["WILDCARD",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningRepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanningRepositoryFilterType:
    return cast(ScanningRepositoryFilterType, data)
