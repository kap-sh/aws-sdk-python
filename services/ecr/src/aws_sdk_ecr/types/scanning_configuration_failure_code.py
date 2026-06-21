"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningConfigurationFailureCode``."""

from typing import Literal, TypeAlias, cast

ScanningConfigurationFailureCode: TypeAlias = Literal["REPOSITORY_NOT_FOUND",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanningConfigurationFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanningConfigurationFailureCode:
    return cast(ScanningConfigurationFailureCode, data)
