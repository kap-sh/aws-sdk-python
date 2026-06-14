"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListToMap``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.flatten
    import aws_sdk_cloudwatch_logs.types.flattened_element
    import aws_sdk_cloudwatch_logs.types.key
    import aws_sdk_cloudwatch_logs.types.source
    import aws_sdk_cloudwatch_logs.types.target
    import aws_sdk_cloudwatch_logs.types.value_key


class ListToMap(TypedDict):
    source: "aws_sdk_cloudwatch_logs.types.source.Source"
    """<p>The key in the log event that has a list of objects that will be converted to a map.</p>"""
    key: "aws_sdk_cloudwatch_logs.types.key.Key"
    """<p>The key of the field to be extracted as keys in the generated map</p>"""
    value_key: NotRequired["aws_sdk_cloudwatch_logs.types.value_key.ValueKey"]
    """<p>If this is specified, the values that you specify in this parameter will be extracted from the <code>source</code> objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map.</p>"""
    target: NotRequired["aws_sdk_cloudwatch_logs.types.target.Target"]
    """<p>The key of the field that will hold the generated map </p>"""
    flatten: "aws_sdk_cloudwatch_logs.types.flatten.Flatten"
    """<p>A Boolean value to indicate whether the list will be flattened into single items. Specify <code>true</code> to flatten the list. The default is <code>false</code> </p>"""
    flattened_element: NotRequired[
        "aws_sdk_cloudwatch_logs.types.flattened_element.FlattenedElement"
    ]
    """<p>If you set <code>flatten</code> to <code>true</code>, use <code>flattenedElement</code> to specify which element, <code>first</code> or <code>last</code>, to keep. </p> <p>You must specify this parameter if <code>flatten</code> is <code>true</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListToMap) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["key"] = value["key"]
    if "value_key" in value:
        out["valueKey"] = value["value_key"]
    if "target" in value:
        out["target"] = value["target"]
    out["flatten"] = value.get("flatten", False)
    if "flattened_element" in value:
        import aws_sdk_cloudwatch_logs.types.flattened_element

        out["flattenedElement"] = (
            aws_sdk_cloudwatch_logs.types.flattened_element.serialize_aws_json_1_1(
                value["flattened_element"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListToMap:
    out: ListToMap = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("ListToMap.source required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ListToMap.key required")
    if "valueKey" in data:
        out["value_key"] = data["valueKey"]
    if "target" in data:
        out["target"] = data["target"]
    if "flatten" in data:
        out["flatten"] = data["flatten"]
    else:
        out["flatten"] = False
    if "flattenedElement" in data:
        import aws_sdk_cloudwatch_logs.types.flattened_element

        out["flattened_element"] = (
            aws_sdk_cloudwatch_logs.types.flattened_element.deserialize_aws_json_1_1(
                data["flattenedElement"]
            )
        )
    return out
