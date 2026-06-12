"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

RecommendationType: TypeAlias = Literal[
    "DKIM",
    "DMARC",
    "SPF",
    "BIMI",
    "COMPLAINT",
    "BOUNCE",
    "FEEDBACK_3P",
    "IP_LISTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DKIM",
        "DMARC",
        "SPF",
        "BIMI",
        "COMPLAINT",
        "BOUNCE",
        "FEEDBACK_3P",
        "IP_LISTING",
    )
)


def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationType value: {data!r}")
    return cast(RecommendationType, data)
