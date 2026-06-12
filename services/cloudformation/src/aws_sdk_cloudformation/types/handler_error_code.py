"""Generated from Smithy shape ``com.amazonaws.cloudformation#HandlerErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HandlerErrorCode: TypeAlias = Literal[
    "NotUpdatable",
    "InvalidRequest",
    "AccessDenied",
    "InvalidCredentials",
    "AlreadyExists",
    "NotFound",
    "ResourceConflict",
    "Throttling",
    "ServiceLimitExceeded",
    "NotStabilized",
    "GeneralServiceException",
    "ServiceInternalError",
    "NetworkFailure",
    "InternalFailure",
    "InvalidTypeConfiguration",
    "HandlerInternalFailure",
    "NonCompliant",
    "Unknown",
    "UnsupportedTarget",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotUpdatable",
        "InvalidRequest",
        "AccessDenied",
        "InvalidCredentials",
        "AlreadyExists",
        "NotFound",
        "ResourceConflict",
        "Throttling",
        "ServiceLimitExceeded",
        "NotStabilized",
        "GeneralServiceException",
        "ServiceInternalError",
        "NetworkFailure",
        "InternalFailure",
        "InvalidTypeConfiguration",
        "HandlerInternalFailure",
        "NonCompliant",
        "Unknown",
        "UnsupportedTarget",
    )
)


def to_query_text(value: HandlerErrorCode) -> str:
    return value


def from_query_text(text: str) -> HandlerErrorCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HandlerErrorCode value: {text!r}")
    return cast(HandlerErrorCode, text)


def serialize_query(
    value: HandlerErrorCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HandlerErrorCode:
    return from_query_text(el.text or "")
