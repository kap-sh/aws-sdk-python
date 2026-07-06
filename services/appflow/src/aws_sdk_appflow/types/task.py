"""Generated from Smithy shape ``com.amazonaws.appflow#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_operator
    import aws_sdk_appflow.types.destination_field
    import aws_sdk_appflow.types.source_fields
    import aws_sdk_appflow.types.task_properties_map
    import aws_sdk_appflow.types.task_type


class Task(TypedDict, closed=True):
    source_fields: "aws_sdk_appflow.types.source_fields.SourceFields"
    """<p> The source fields to which a particular task is applied. </p>"""
    connector_operator: NotRequired[
        "aws_sdk_appflow.types.connector_operator.ConnectorOperator"
    ]
    """<p> The operation to be performed on the provided source fields. </p>"""
    destination_field: NotRequired[
        "aws_sdk_appflow.types.destination_field.DestinationField"
    ]
    """<p> A field in a destination connector, or a field value against which Amazon AppFlow validates a source field. </p>"""
    task_type: "aws_sdk_appflow.types.task_type.TaskType"
    """<p> Specifies the particular task implementation that Amazon AppFlow performs. </p>"""
    task_properties: NotRequired[
        "aws_sdk_appflow.types.task_properties_map.TaskPropertiesMap"
    ]
    """<p> A map used to store task-related information. The execution service looks for particular information based on the <code>TaskType</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Task) -> dict:
    out: dict = {}
    import aws_sdk_appflow.types.source_fields

    out["sourceFields"] = aws_sdk_appflow.types.source_fields.serialize_json(
        value["source_fields"]
    )
    if "connector_operator" in value:
        import aws_sdk_appflow.types.connector_operator

        out["connectorOperator"] = (
            aws_sdk_appflow.types.connector_operator.serialize_json(
                value["connector_operator"]
            )
        )
    if "destination_field" in value:
        out["destinationField"] = value["destination_field"]
    import aws_sdk_appflow.types.task_type

    out["taskType"] = aws_sdk_appflow.types.task_type.serialize_json(value["task_type"])
    if "task_properties" in value:
        import aws_sdk_appflow.types.task_properties_map

        out["taskProperties"] = (
            aws_sdk_appflow.types.task_properties_map.serialize_json(
                value["task_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if "sourceFields" in data:
        import aws_sdk_appflow.types.source_fields

        out["source_fields"] = aws_sdk_appflow.types.source_fields.deserialize_json(
            data["sourceFields"]
        )
    else:
        raise DeserializationError("Task.source_fields required")
    if "connectorOperator" in data:
        import aws_sdk_appflow.types.connector_operator

        out["connector_operator"] = (
            aws_sdk_appflow.types.connector_operator.deserialize_json(
                data["connectorOperator"]
            )
        )
    if "destinationField" in data:
        out["destination_field"] = data["destinationField"]
    if "taskType" in data:
        import aws_sdk_appflow.types.task_type

        out["task_type"] = aws_sdk_appflow.types.task_type.deserialize_json(
            data["taskType"]
        )
    else:
        raise DeserializationError("Task.task_type required")
    if "taskProperties" in data:
        import aws_sdk_appflow.types.task_properties_map

        out["task_properties"] = (
            aws_sdk_appflow.types.task_properties_map.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
