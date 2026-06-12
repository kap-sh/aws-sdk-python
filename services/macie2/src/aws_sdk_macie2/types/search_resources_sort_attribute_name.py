"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesSortAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to sort the query results by. Valid values are:</p>"""
SearchResourcesSortAttributeName: TypeAlias = Literal[
    "ACCOUNT_ID",
    "RESOURCE_NAME",
    "S3_CLASSIFIABLE_OBJECT_COUNT",
    "S3_CLASSIFIABLE_SIZE_IN_BYTES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "RESOURCE_NAME",
        "S3_CLASSIFIABLE_OBJECT_COUNT",
        "S3_CLASSIFIABLE_SIZE_IN_BYTES",
    )
)


def serialize_json(value: SearchResourcesSortAttributeName) -> str:
    return value


def deserialize_json(data: str) -> SearchResourcesSortAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchResourcesSortAttributeName value: {data!r}"
        )
    return cast(SearchResourcesSortAttributeName, data)
