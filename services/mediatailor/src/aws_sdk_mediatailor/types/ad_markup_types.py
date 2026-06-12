"""Generated from Smithy shape ``com.amazonaws.mediatailor#adMarkupTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.ad_markup_type

adMarkupTypes: TypeAlias = list["aws_sdk_mediatailor.types.ad_markup_type.AdMarkupType"]


# --- restJson1 ser/de ---
def serialize_json(value: adMarkupTypes) -> list:
    import aws_sdk_mediatailor.types.ad_markup_type

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.ad_markup_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> adMarkupTypes:
    import aws_sdk_mediatailor.types.ad_markup_type

    out: adMarkupTypes = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.ad_markup_type.deserialize_json(item))
    return out
