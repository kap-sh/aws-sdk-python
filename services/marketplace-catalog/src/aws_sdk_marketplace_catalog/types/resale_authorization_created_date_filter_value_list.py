"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationCreatedDateFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.date_time_iso8601

ResaleAuthorizationCreatedDateFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationCreatedDateFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResaleAuthorizationCreatedDateFilterValueList:
    return list(data)
