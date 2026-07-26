"""Generated from Smithy shape ``com.amazonaws.iot#HttpHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.http_header_name
    import capo_iot.types.http_header_value

HttpHeaders: TypeAlias = dict[
    "capo_iot.types.http_header_name.HttpHeaderName",
    "capo_iot.types.http_header_value.HttpHeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HttpHeaders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HttpHeaders:
    out: HttpHeaders = {}
    for key, value in data.items():
        out[key] = value
    return out
