"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppBlockBuilderStateChangeReasonCode: TypeAlias = Literal["INTERNAL_ERROR",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERNAL_ERROR",))


def serialize_aws_json_1_1(value: AppBlockBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AppBlockBuilderStateChangeReasonCode value: {data!r}"
        )
    return cast(AppBlockBuilderStateChangeReasonCode, data)
