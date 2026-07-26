"""Generated from Smithy shape ``com.amazonaws.ecs#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.double
    import capo_ecs.types.integer
    import capo_ecs.types.long
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class Resource(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the resource, such as <code>CPU</code>, <code>MEMORY</code>, <code>PORTS</code>, <code>PORTS_UDP</code>, or a user-defined resource.</p>"""
    type: NotRequired["capo_ecs.types.string.String"]
    """<p>The type of the resource. Valid values: <code>INTEGER</code>, <code>DOUBLE</code>, <code>LONG</code>, or <code>STRINGSET</code>.</p>"""
    double_value: "capo_ecs.types.double.Double"
    """<p>When the <code>doubleValue</code> type is set, the value of the resource must be a double precision floating-point type.</p>"""
    long_value: "capo_ecs.types.long.Long"
    """<p>When the <code>longValue</code> type is set, the value of the resource must be an extended precision floating-point type.</p>"""
    integer_value: "capo_ecs.types.integer.Integer"
    """<p>When the <code>integerValue</code> type is set, the value of the resource must be an integer.</p>"""
    string_set_value: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>When the <code>stringSetValue</code> type is set, the value of the resource must be a string type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    out["doubleValue"] = value.get("double_value", 0)
    out["longValue"] = value.get("long_value", 0)
    out["integerValue"] = value.get("integer_value", 0)
    if "string_set_value" in value:
        import capo_ecs.types.string_list

        out["stringSetValue"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["string_set_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "doubleValue" in data:
        out["double_value"] = data["doubleValue"]
    else:
        out["double_value"] = 0
    if "longValue" in data:
        out["long_value"] = data["longValue"]
    else:
        out["long_value"] = 0
    if "integerValue" in data:
        out["integer_value"] = data["integerValue"]
    else:
        out["integer_value"] = 0
    if "stringSetValue" in data:
        import capo_ecs.types.string_list

        out["string_set_value"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["stringSetValue"]
        )
    return out
