"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiNoticeCode``."""

from typing import Literal, TypeAlias, cast

RouteTaxiNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "Other",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiNoticeCode:
    return cast(RouteTaxiNoticeCode, data)
