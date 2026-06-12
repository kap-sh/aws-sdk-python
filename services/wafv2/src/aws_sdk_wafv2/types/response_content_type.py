"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

ResponseContentType: TypeAlias = Literal[
    "TEXT_PLAIN",
    "TEXT_HTML",
    "APPLICATION_JSON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT_PLAIN",
        "TEXT_HTML",
        "APPLICATION_JSON",
    )
)


def serialize_aws_json_1_1(value: ResponseContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResponseContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseContentType value: {data!r}")
    return cast(ResponseContentType, data)
