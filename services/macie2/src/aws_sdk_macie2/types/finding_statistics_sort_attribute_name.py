"""Generated from Smithy shape ``com.amazonaws.macie2#FindingStatisticsSortAttributeName``."""

from typing import Literal, TypeAlias, cast

"""<p>The grouping to sort the results by. Valid values are:</p>"""
FindingStatisticsSortAttributeName: TypeAlias = Literal[
    "groupKey",
    "count",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatisticsSortAttributeName) -> str:
    return value


def deserialize_json(data: str) -> FindingStatisticsSortAttributeName:
    return cast(FindingStatisticsSortAttributeName, data)
