"""Generated from Smithy shape ``com.amazonaws.iot#HttpActionHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.header_key
    import aws_sdk_iot.types.header_value


class HttpActionHeader(TypedDict, closed=True):
    key: "aws_sdk_iot.types.header_key.HeaderKey"
    """<p>The HTTP header key.</p>"""
    value: "aws_sdk_iot.types.header_value.HeaderValue"
    """<p>The HTTP header value. Substitution templates are supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpActionHeader) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HttpActionHeader:
    out: HttpActionHeader = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("HttpActionHeader.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("HttpActionHeader.value required")
    return out
