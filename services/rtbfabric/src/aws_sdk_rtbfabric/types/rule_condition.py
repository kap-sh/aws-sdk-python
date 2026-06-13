"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RuleCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.query_string_key_value_pair


class RuleCondition(TypedDict):
    host_header: NotRequired["str"]
    """<p>The exact host header value to match.</p>"""
    host_header_wildcard: NotRequired["str"]
    """<p>A wildcard pattern for host header matching (for example, <code>*.example.com</code>).</p>"""
    path_prefix: NotRequired["str"]
    """<p>The path prefix to match. The request path must start with this value. Must start with <code>/</code>.</p>"""
    path_exact: NotRequired["str"]
    """<p>The exact path to match. Must start with <code>/</code>.</p>"""
    query_string_equals: NotRequired[
        "aws_sdk_rtbfabric.types.query_string_key_value_pair.QueryStringKeyValuePair"
    ]
    """<p>A query string key-value pair that must be present and match exactly.</p>"""
    query_string_exists: NotRequired["str"]
    """<p>A query string key that must be present in the request (any value is accepted).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleCondition) -> dict:
    out: dict = {}
    if "host_header" in value:
        out["hostHeader"] = value["host_header"]
    if "host_header_wildcard" in value:
        out["hostHeaderWildcard"] = value["host_header_wildcard"]
    if "path_prefix" in value:
        out["pathPrefix"] = value["path_prefix"]
    if "path_exact" in value:
        out["pathExact"] = value["path_exact"]
    if "query_string_equals" in value:
        import aws_sdk_rtbfabric.types.query_string_key_value_pair

        out["queryStringEquals"] = (
            aws_sdk_rtbfabric.types.query_string_key_value_pair.serialize_json(
                value["query_string_equals"]
            )
        )
    if "query_string_exists" in value:
        out["queryStringExists"] = value["query_string_exists"]
    return out


def deserialize_json(data: dict) -> RuleCondition:
    out: RuleCondition = {}  # type: ignore[typeddict-item]
    if "hostHeader" in data:
        out["host_header"] = data["hostHeader"]
    if "hostHeaderWildcard" in data:
        out["host_header_wildcard"] = data["hostHeaderWildcard"]
    if "pathPrefix" in data:
        out["path_prefix"] = data["pathPrefix"]
    if "pathExact" in data:
        out["path_exact"] = data["pathExact"]
    if "queryStringEquals" in data:
        import aws_sdk_rtbfabric.types.query_string_key_value_pair

        out["query_string_equals"] = (
            aws_sdk_rtbfabric.types.query_string_key_value_pair.deserialize_json(
                data["queryStringEquals"]
            )
        )
    if "queryStringExists" in data:
        out["query_string_exists"] = data["queryStringExists"]
    return out
