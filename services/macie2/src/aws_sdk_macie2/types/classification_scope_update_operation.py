"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationScopeUpdateOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies how to apply changes to the S3 bucket exclusion list defined by the classification scope for an Amazon Macie account. Valid values are:</p>"""
ClassificationScopeUpdateOperation: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "REMOVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "REPLACE",
        "REMOVE",
    )
)


def serialize_json(value: ClassificationScopeUpdateOperation) -> str:
    return value


def deserialize_json(data: str) -> ClassificationScopeUpdateOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClassificationScopeUpdateOperation value: {data!r}"
        )
    return cast(ClassificationScopeUpdateOperation, data)
