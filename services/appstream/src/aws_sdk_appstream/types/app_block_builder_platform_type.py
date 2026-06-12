"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderPlatformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppBlockBuilderPlatformType: TypeAlias = Literal["WINDOWS_SERVER_2019",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WINDOWS_SERVER_2019",))


def serialize_aws_json_1_1(value: AppBlockBuilderPlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderPlatformType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AppBlockBuilderPlatformType value: {data!r}"
        )
    return cast(AppBlockBuilderPlatformType, data)
