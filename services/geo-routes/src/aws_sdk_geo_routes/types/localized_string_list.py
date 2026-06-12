"""Generated from Smithy shape ``com.amazonaws.georoutes#LocalizedStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string

LocalizedStringList: TypeAlias = list[
    "aws_sdk_geo_routes.types.localized_string.LocalizedString"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedStringList) -> list:
    import aws_sdk_geo_routes.types.localized_string

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.localized_string.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocalizedStringList:
    import aws_sdk_geo_routes.types.localized_string

    out: LocalizedStringList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.localized_string.deserialize_json(item))
    return out
