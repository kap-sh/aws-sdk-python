"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionQueryStringParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.boolean
    import capo_cloudwatch_events.types.query_string_key
    import capo_cloudwatch_events.types.query_string_value_sensitive


class ConnectionQueryStringParameter(TypedDict, closed=True):
    key: NotRequired["capo_cloudwatch_events.types.query_string_key.QueryStringKey"]
    """<p>The key for a query string parameter.</p>"""
    value: NotRequired[
        "capo_cloudwatch_events.types.query_string_value_sensitive.QueryStringValueSensitive"
    ]
    """<p>The value associated with the key for the query string parameter.</p>"""
    is_value_secret: "capo_cloudwatch_events.types.boolean.Boolean"
    """<p>Specifies whether the value is secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionQueryStringParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["IsValueSecret"] = value.get("is_value_secret", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionQueryStringParameter:
    out: ConnectionQueryStringParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "IsValueSecret" in data:
        out["is_value_secret"] = data["IsValueSecret"]
    else:
        out["is_value_secret"] = False
    return out
