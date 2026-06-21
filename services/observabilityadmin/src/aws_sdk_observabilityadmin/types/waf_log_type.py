"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#WAFLogType``."""

from typing import Literal, TypeAlias, cast

"""<p> Enumeration of supported WAF log types. Currently only WAF_LOGS is supported. </p>"""
WAFLogType: TypeAlias = Literal["WAF_LOGS",]


# --- restJson1 ser/de ---
def serialize_json(value: WAFLogType) -> str:
    return value


def deserialize_json(data: str) -> WAFLogType:
    return cast(WAFLogType, data)
