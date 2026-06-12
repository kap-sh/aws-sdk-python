"""Generated from Smithy shape ``com.amazonaws.macie2#AllowListStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Indicates the current status of an allow list. Depending on the type of criteria that the list specifies, possible values are:</p>"""
AllowListStatusCode: TypeAlias = Literal[
    "OK",
    "S3_OBJECT_NOT_FOUND",
    "S3_USER_ACCESS_DENIED",
    "S3_OBJECT_ACCESS_DENIED",
    "S3_THROTTLED",
    "S3_OBJECT_OVERSIZE",
    "S3_OBJECT_EMPTY",
    "UNKNOWN_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "S3_OBJECT_NOT_FOUND",
        "S3_USER_ACCESS_DENIED",
        "S3_OBJECT_ACCESS_DENIED",
        "S3_THROTTLED",
        "S3_OBJECT_OVERSIZE",
        "S3_OBJECT_EMPTY",
        "UNKNOWN_ERROR",
    )
)


def serialize_json(value: AllowListStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AllowListStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowListStatusCode value: {data!r}")
    return cast(AllowListStatusCode, data)
