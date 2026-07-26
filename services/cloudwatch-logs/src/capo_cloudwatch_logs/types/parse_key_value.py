"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseKeyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination_field
    import capo_cloudwatch_logs.types.key_prefix
    import capo_cloudwatch_logs.types.key_value_delimiter
    import capo_cloudwatch_logs.types.non_match_value
    import capo_cloudwatch_logs.types.overwrite_if_exists
    import capo_cloudwatch_logs.types.parser_field_delimiter
    import capo_cloudwatch_logs.types.source


class ParseKeyValue(TypedDict, closed=True):
    source: NotRequired["capo_cloudwatch_logs.types.source.Source"]
    """<p>Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, <code>store.book</code> </p>"""
    destination: NotRequired[
        "capo_cloudwatch_logs.types.destination_field.DestinationField"
    ]
    """<p>The destination field to put the extracted key-value pairs into</p>"""
    field_delimiter: NotRequired[
        "capo_cloudwatch_logs.types.parser_field_delimiter.ParserFieldDelimiter"
    ]
    """<p>The field delimiter string that is used between key-value pairs in the original log events. If you omit this, the ampersand <code>&</code> character is used.</p>"""
    key_value_delimiter: NotRequired[
        "capo_cloudwatch_logs.types.key_value_delimiter.KeyValueDelimiter"
    ]
    """<p>The delimiter string to use between the key and value in each pair in the transformed log event.</p> <p> If you omit this, the equal <code>=</code> character is used.</p>"""
    key_prefix: NotRequired["capo_cloudwatch_logs.types.key_prefix.KeyPrefix"]
    """<p>If you want to add a prefix to all transformed keys, specify it here.</p>"""
    non_match_value: NotRequired[
        "capo_cloudwatch_logs.types.non_match_value.NonMatchValue"
    ]
    """<p>A value to insert into the value field in the result, when a key-value pair is not successfully split.</p>"""
    overwrite_if_exists: (
        "capo_cloudwatch_logs.types.overwrite_if_exists.OverwriteIfExists"
    )
    """<p>Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseKeyValue) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "field_delimiter" in value:
        out["fieldDelimiter"] = value["field_delimiter"]
    if "key_value_delimiter" in value:
        out["keyValueDelimiter"] = value["key_value_delimiter"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    if "non_match_value" in value:
        out["nonMatchValue"] = value["non_match_value"]
    out["overwriteIfExists"] = value.get("overwrite_if_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseKeyValue:
    out: ParseKeyValue = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "fieldDelimiter" in data:
        out["field_delimiter"] = data["fieldDelimiter"]
    if "keyValueDelimiter" in data:
        out["key_value_delimiter"] = data["keyValueDelimiter"]
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    if "nonMatchValue" in data:
        out["non_match_value"] = data["nonMatchValue"]
    if "overwriteIfExists" in data:
        out["overwrite_if_exists"] = data["overwriteIfExists"]
    else:
        out["overwrite_if_exists"] = False
    return out
