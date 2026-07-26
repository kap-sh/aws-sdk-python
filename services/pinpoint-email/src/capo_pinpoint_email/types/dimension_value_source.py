"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DimensionValueSource``."""

from typing import Literal, TypeAlias, cast

"""<p>The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon Pinpoint to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose <code>messageTag</code>. If you want Amazon Pinpoint to use your own email headers, choose <code>emailHeader</code>. If you want Amazon Pinpoint to use link tags, choose <code>linkTags</code>.</p>"""
DimensionValueSource: TypeAlias = Literal[
    "MESSAGE_TAG",
    "EMAIL_HEADER",
    "LINK_TAG",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionValueSource) -> str:
    return value


def deserialize_json(data: str) -> DimensionValueSource:
    return cast(DimensionValueSource, data)
