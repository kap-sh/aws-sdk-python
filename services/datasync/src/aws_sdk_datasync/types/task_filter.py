"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_values
    import aws_sdk_datasync.types.operator
    import aws_sdk_datasync.types.task_filter_name


class TaskFilter(TypedDict):
    name: "aws_sdk_datasync.types.task_filter_name.TaskFilterName"
    """<p>The name of the filter being used. Each API call supports a list of filters that are available for it. For example, <code>LocationId</code> for <code>ListTasks</code>.</p>"""
    values: "aws_sdk_datasync.types.filter_values.FilterValues"
    """<p>The values that you want to filter for. For example, you might want to display only tasks for a specific destination location.</p>"""
    operator: "aws_sdk_datasync.types.operator.Operator"
    """<p>The operator that is used to compare filter values (for example, <code>Equals</code> or <code>Contains</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilter) -> dict:
    out: dict = {}
    import aws_sdk_datasync.types.task_filter_name

    out["Name"] = aws_sdk_datasync.types.task_filter_name.serialize_aws_json_1_1(
        value["name"]
    )
    import aws_sdk_datasync.types.filter_values

    out["Values"] = aws_sdk_datasync.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import aws_sdk_datasync.types.operator

    out["Operator"] = aws_sdk_datasync.types.operator.serialize_aws_json_1_1(
        value["operator"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskFilter:
    out: TaskFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_datasync.types.task_filter_name

        out["name"] = aws_sdk_datasync.types.task_filter_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    else:
        raise DeserializationError("TaskFilter.name required")
    if "Values" in data:
        import aws_sdk_datasync.types.filter_values

        out["values"] = aws_sdk_datasync.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("TaskFilter.values required")
    if "Operator" in data:
        import aws_sdk_datasync.types.operator

        out["operator"] = aws_sdk_datasync.types.operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    else:
        raise DeserializationError("TaskFilter.operator required")
    return out
