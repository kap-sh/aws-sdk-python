"""Generated from Smithy shape ``com.amazonaws.connect#FilterV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.filter_v2_string_condition
    import aws_sdk_connect.types.filter_value_list
    import aws_sdk_connect.types.resource_arn_or_id


class FilterV2(TypedDict, closed=True):
    filter_key: NotRequired["aws_sdk_connect.types.resource_arn_or_id.ResourceArnOrId"]
    """<p>The key to use for filtering data. For example, <code>QUEUE</code>, <code>ROUTING_PROFILE, AGENT</code>, <code>CHANNEL</code>, <code>AGENT_HIERARCHY_LEVEL_ONE</code>, <code>AGENT_HIERARCHY_LEVEL_TWO</code>, <code>AGENT_HIERARCHY_LEVEL_THREE</code>, <code>AGENT_HIERARCHY_LEVEL_FOUR</code>, <code>AGENT_HIERARCHY_LEVEL_FIVE</code>. There must be at least 1 key and a maximum 5 keys. </p>"""
    filter_values: NotRequired[
        "aws_sdk_connect.types.filter_value_list.FilterValueList"
    ]
    """<p>The identifiers to use for filtering data. For example, if you have a filter key of <code>QUEUE</code>, you would add queue IDs or ARNs in <code>FilterValues</code>. </p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.filter_v2_string_condition.FilterV2StringCondition"
    ]
    """<p> System defined filtering condition. For example, the NOT_EXISTS StringCondition returns documents where the field specified by FilterKey does not exist in the document.</p> <p>When the NOT_EXISTS StringCondition is added to a FilterV2 object, FilterValues must be null or empty. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterV2) -> dict:
    out: dict = {}
    if "filter_key" in value:
        out["FilterKey"] = value["filter_key"]
    if "filter_values" in value:
        import aws_sdk_connect.types.filter_value_list

        out["FilterValues"] = aws_sdk_connect.types.filter_value_list.serialize_json(
            value["filter_values"]
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.filter_v2_string_condition

        out["StringCondition"] = (
            aws_sdk_connect.types.filter_v2_string_condition.serialize_json(
                value["string_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterV2:
    out: FilterV2 = {}  # type: ignore[typeddict-item]
    if "FilterKey" in data:
        out["filter_key"] = data["FilterKey"]
    if "FilterValues" in data:
        import aws_sdk_connect.types.filter_value_list

        out["filter_values"] = aws_sdk_connect.types.filter_value_list.deserialize_json(
            data["FilterValues"]
        )
    if "StringCondition" in data:
        import aws_sdk_connect.types.filter_v2_string_condition

        out["string_condition"] = (
            aws_sdk_connect.types.filter_v2_string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    return out
