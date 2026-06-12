"""Generated from Smithy shape ``com.amazonaws.macie2#FindingStatisticsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The grouping to sort the results by. Valid values are:</p>"""
FindingStatisticsSortAttributeName: TypeAlias = Literal[
    "groupKey",
    "count",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "groupKey",
        "count",
    )
)


def serialize_json(value: FindingStatisticsSortAttributeName) -> str:
    return value


def deserialize_json(data: str) -> FindingStatisticsSortAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FindingStatisticsSortAttributeName value: {data!r}"
        )
    return cast(FindingStatisticsSortAttributeName, data)
