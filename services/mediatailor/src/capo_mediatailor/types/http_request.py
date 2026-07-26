"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.compression_method
    import capo_mediatailor.types.method
    import capo_mediatailor.types.string_map


class HttpRequest(TypedDict, closed=True):
    method: NotRequired["capo_mediatailor.types.method.Method"]
    """<p>The HTTP method to use when making requests to the ad decision server. Supported values are <code>GET</code> and <code>POST</code>.</p>"""
    body: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The request body content to send with HTTP requests to the ad decision server. This value is only eligible for <code>POST</code> requests.</p>"""
    headers: NotRequired["capo_mediatailor.types.string_map.StringMap"]
    """<p>Custom HTTP headers to include in requests to the ad decision server. Specify headers as key-value pairs. This value is only eligible for <code>POST</code> requests.</p>"""
    compress_request: NotRequired[
        "capo_mediatailor.types.compression_method.CompressionMethod"
    ]
    """<p>The compression method to apply to requests sent to the ad decision server. Supported values are <code>NONE</code> and <code>GZIP</code>. This value is only eligible for <code>POST</code> requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRequest) -> dict:
    out: dict = {}
    if "method" in value:
        import capo_mediatailor.types.method

        out["Method"] = capo_mediatailor.types.method.serialize_json(value["method"])
    if "body" in value:
        out["Body"] = value["body"]
    if "headers" in value:
        import capo_mediatailor.types.string_map

        out["Headers"] = capo_mediatailor.types.string_map.serialize_json(
            value["headers"]
        )
    if "compress_request" in value:
        import capo_mediatailor.types.compression_method

        out["CompressRequest"] = (
            capo_mediatailor.types.compression_method.serialize_json(
                value["compress_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpRequest:
    out: HttpRequest = {}  # type: ignore[typeddict-item]
    if "Method" in data:
        import capo_mediatailor.types.method

        out["method"] = capo_mediatailor.types.method.deserialize_json(data["Method"])
    if "Body" in data:
        out["body"] = data["Body"]
    if "Headers" in data:
        import capo_mediatailor.types.string_map

        out["headers"] = capo_mediatailor.types.string_map.deserialize_json(
            data["Headers"]
        )
    if "CompressRequest" in data:
        import capo_mediatailor.types.compression_method

        out["compress_request"] = (
            capo_mediatailor.types.compression_method.deserialize_json(
                data["CompressRequest"]
            )
        )
    return out
