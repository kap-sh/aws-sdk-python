"""Generated from Smithy shape ``com.amazonaws.securityhub#KeywordFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.keyword_filter

KeywordFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.keyword_filter.KeywordFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: KeywordFilterList) -> list:
    import aws_sdk_securityhub.types.keyword_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.keyword_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> KeywordFilterList:
    import aws_sdk_securityhub.types.keyword_filter

    out: KeywordFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.keyword_filter.deserialize_json(item))
    return out
