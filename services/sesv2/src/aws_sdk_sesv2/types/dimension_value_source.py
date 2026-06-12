"""Generated from Smithy shape ``com.amazonaws.sesv2#DimensionValueSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The location where the Amazon SES API v2 finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an <code>X-SES-MESSAGE-TAGS</code> header or a parameter to the <code>SendEmail</code> or <code>SendRawEmail</code> API, choose <code>messageTag</code>. To use your own email headers, choose <code>emailHeader</code>. To use link tags, choose <code>linkTags</code>.</p>"""
DimensionValueSource: TypeAlias = Literal[
    "MESSAGE_TAG",
    "EMAIL_HEADER",
    "LINK_TAG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MESSAGE_TAG",
        "EMAIL_HEADER",
        "LINK_TAG",
    )
)


def serialize_json(value: DimensionValueSource) -> str:
    return value


def deserialize_json(data: str) -> DimensionValueSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionValueSource value: {data!r}")
    return cast(DimensionValueSource, data)
