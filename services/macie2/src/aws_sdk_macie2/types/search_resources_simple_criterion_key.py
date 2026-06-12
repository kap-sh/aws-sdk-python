"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesSimpleCriterionKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to use in a condition that filters the query results. Valid values are:</p>"""
SearchResourcesSimpleCriterionKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "S3_BUCKET_NAME",
    "S3_BUCKET_EFFECTIVE_PERMISSION",
    "S3_BUCKET_SHARED_ACCESS",
    "AUTOMATED_DISCOVERY_MONITORING_STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "S3_BUCKET_NAME",
        "S3_BUCKET_EFFECTIVE_PERMISSION",
        "S3_BUCKET_SHARED_ACCESS",
        "AUTOMATED_DISCOVERY_MONITORING_STATUS",
    )
)


def serialize_json(value: SearchResourcesSimpleCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> SearchResourcesSimpleCriterionKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchResourcesSimpleCriterionKey value: {data!r}"
        )
    return cast(SearchResourcesSimpleCriterionKey, data)
