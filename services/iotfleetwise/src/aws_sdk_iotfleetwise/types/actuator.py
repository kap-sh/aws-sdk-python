"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Actuator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.double
    import aws_sdk_iotfleetwise.types.list_of_strings
    import aws_sdk_iotfleetwise.types.message
    import aws_sdk_iotfleetwise.types.node_data_type
    import aws_sdk_iotfleetwise.types.node_path
    import aws_sdk_iotfleetwise.types.string


class Actuator(TypedDict, closed=True):
    fully_qualified_name: "aws_sdk_iotfleetwise.types.string.string"
    """<p>The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be <code>Vehicle.Front.Left.Door.Lock</code>.</p>"""
    data_type: "aws_sdk_iotfleetwise.types.node_data_type.NodeDataType"
    """<p>The specified data type of the actuator. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the actuator.</p>"""
    unit: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>The scientific unit for the actuator.</p>"""
    allowed_values: NotRequired[
        "aws_sdk_iotfleetwise.types.list_of_strings.listOfStrings"
    ]
    """<p>A list of possible values an actuator can take.</p>"""
    min: NotRequired["aws_sdk_iotfleetwise.types.double.double"]
    """<p>The specified possible minimum value of an actuator.</p>"""
    max: NotRequired["aws_sdk_iotfleetwise.types.double.double"]
    """<p>The specified possible maximum value of an actuator.</p>"""
    assigned_value: NotRequired["aws_sdk_iotfleetwise.types.string.string"]
    """<p>A specified value for the actuator.</p>"""
    deprecation_message: NotRequired["aws_sdk_iotfleetwise.types.message.message"]
    """<p>The deprecation message for the node or the branch that was moved or deleted.</p>"""
    comment: NotRequired["aws_sdk_iotfleetwise.types.message.message"]
    """<p>A comment in addition to the description.</p>"""
    struct_fully_qualified_name: NotRequired[
        "aws_sdk_iotfleetwise.types.node_path.NodePath"
    ]
    """<p>The fully qualified name of the struct node for the actuator if the data type of the actuator is <code>Struct</code> or <code>StructArray</code>. For example, the struct fully qualified name of an actuator might be <code>Vehicle.Door.LockStruct</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Actuator) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import aws_sdk_iotfleetwise.types.node_data_type

    out["dataType"] = aws_sdk_iotfleetwise.types.node_data_type.serialize_aws_json_1_0(
        value["data_type"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "allowed_values" in value:
        import aws_sdk_iotfleetwise.types.list_of_strings

        out["allowedValues"] = (
            aws_sdk_iotfleetwise.types.list_of_strings.serialize_aws_json_1_0(
                value["allowed_values"]
            )
        )
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    if "assigned_value" in value:
        out["assignedValue"] = value["assigned_value"]
    if "deprecation_message" in value:
        out["deprecationMessage"] = value["deprecation_message"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "struct_fully_qualified_name" in value:
        out["structFullyQualifiedName"] = value["struct_fully_qualified_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Actuator:
    out: Actuator = {}  # type: ignore[typeddict-item]
    if "fullyQualifiedName" in data:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError("Actuator.fully_qualified_name required")
    if "dataType" in data:
        import aws_sdk_iotfleetwise.types.node_data_type

        out["data_type"] = (
            aws_sdk_iotfleetwise.types.node_data_type.deserialize_aws_json_1_0(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("Actuator.data_type required")
    if "description" in data:
        out["description"] = data["description"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "allowedValues" in data:
        import aws_sdk_iotfleetwise.types.list_of_strings

        out["allowed_values"] = (
            aws_sdk_iotfleetwise.types.list_of_strings.deserialize_aws_json_1_0(
                data["allowedValues"]
            )
        )
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    if "assignedValue" in data:
        out["assigned_value"] = data["assignedValue"]
    if "deprecationMessage" in data:
        out["deprecation_message"] = data["deprecationMessage"]
    if "comment" in data:
        out["comment"] = data["comment"]
    if "structFullyQualifiedName" in data:
        out["struct_fully_qualified_name"] = data["structFullyQualifiedName"]
    return out
