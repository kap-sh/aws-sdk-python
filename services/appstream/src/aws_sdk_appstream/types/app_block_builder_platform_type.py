"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderPlatformType``."""

from typing import Literal, TypeAlias, cast

AppBlockBuilderPlatformType: TypeAlias = Literal["WINDOWS_SERVER_2019",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderPlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderPlatformType:
    return cast(AppBlockBuilderPlatformType, data)
