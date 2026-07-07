"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FieldToMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.single_header


class FieldToMatch(TypedDict, closed=True):
    single_header: NotRequired[
        "aws_sdk_observabilityadmin.types.single_header.SingleHeader"
    ]
    """<p> Redacts a specific header field by name from WAF logs. </p>"""
    uri_path: NotRequired["str"]
    """<p> Redacts the URI path from WAF logs. </p>"""
    query_string: NotRequired["str"]
    """<p> Redacts the entire query string from WAF logs. </p>"""
    method: NotRequired["str"]
    """<p> Redacts the HTTP method from WAF logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldToMatch) -> dict:
    out: dict = {}
    if "single_header" in value:
        import aws_sdk_observabilityadmin.types.single_header

        out["SingleHeader"] = (
            aws_sdk_observabilityadmin.types.single_header.serialize_json(
                value["single_header"]
            )
        )
    if "uri_path" in value:
        out["UriPath"] = value["uri_path"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "method" in value:
        out["Method"] = value["method"]
    return out


def deserialize_json(data: dict) -> FieldToMatch:
    out: FieldToMatch = {}  # type: ignore[typeddict-item]
    if "SingleHeader" in data:
        import aws_sdk_observabilityadmin.types.single_header

        out["single_header"] = (
            aws_sdk_observabilityadmin.types.single_header.deserialize_json(
                data["SingleHeader"]
            )
        )
    if "UriPath" in data:
        out["uri_path"] = data["UriPath"]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    if "Method" in data:
        out["method"] = data["Method"]
    return out
