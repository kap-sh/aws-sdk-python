"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported, which represent resources in your Amazon SES account that have reputation tracking capabilities.</p>"""
ReputationEntityType: TypeAlias = Literal["RESOURCE",]


# --- restJson1 ser/de ---
def serialize_json(value: ReputationEntityType) -> str:
    return value


def deserialize_json(data: str) -> ReputationEntityType:
    return cast(ReputationEntityType, data)
