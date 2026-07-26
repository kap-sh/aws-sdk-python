"""Generated from Smithy shape ``com.amazonaws.cloudformation#HandlerErrorCode``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

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
def to_query_text(value: HandlerErrorCode) -> str:
    return value


def from_query_text(text: str) -> HandlerErrorCode:
    return cast(HandlerErrorCode, text)


def serialize_query(
    value: HandlerErrorCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HandlerErrorCode:
    return from_query_text(el.text or "")
