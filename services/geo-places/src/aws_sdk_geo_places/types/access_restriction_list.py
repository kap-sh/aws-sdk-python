"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessRestrictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.access_restriction

AccessRestrictionList: TypeAlias = list[
    "aws_sdk_geo_places.types.access_restriction.AccessRestriction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessRestrictionList) -> list:
    import aws_sdk_geo_places.types.access_restriction

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.access_restriction.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessRestrictionList:
    import aws_sdk_geo_places.types.access_restriction

    out: AccessRestrictionList = []
    for item in data:
        out.append(aws_sdk_geo_places.types.access_restriction.deserialize_json(item))
    return out
