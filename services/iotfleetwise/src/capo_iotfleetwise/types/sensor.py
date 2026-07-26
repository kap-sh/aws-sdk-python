"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Sensor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.double
    import capo_iotfleetwise.types.list_of_strings
    import capo_iotfleetwise.types.message
    import capo_iotfleetwise.types.node_data_type
    import capo_iotfleetwise.types.node_path
    import capo_iotfleetwise.types.string


class Sensor(TypedDict, closed=True):
    fully_qualified_name: "capo_iotfleetwise.types.string.string"
    """<p>The fully qualified name of the sensor. For example, the fully qualified name of a sensor might be <code>Vehicle.Body.Engine.Battery</code>.</p>"""
    data_type: "capo_iotfleetwise.types.node_data_type.NodeDataType"
    """<p>The specified data type of the sensor. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of a sensor.</p>"""
    unit: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The scientific unit of measurement for data collected by the sensor.</p>"""
    allowed_values: NotRequired["capo_iotfleetwise.types.list_of_strings.listOfStrings"]
    """<p>A list of possible values a sensor can take.</p>"""
    min: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>The specified possible minimum value of the sensor.</p>"""
    max: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>The specified possible maximum value of the sensor.</p>"""
    deprecation_message: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>The deprecation message for the node or the branch that was moved or deleted.</p>"""
    comment: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>A comment in addition to the description.</p>"""
    struct_fully_qualified_name: NotRequired[
        "capo_iotfleetwise.types.node_path.NodePath"
    ]
    """<p>The fully qualified name of the struct node for a sensor if the data type of the actuator is <code>Struct</code> or <code>StructArray</code>. For example, the struct fully qualified name of a sensor might be <code>Vehicle.ADAS.CameraStruct</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Sensor) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import capo_iotfleetwise.types.node_data_type

    out["dataType"] = capo_iotfleetwise.types.node_data_type.serialize_aws_json_1_0(
        value["data_type"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "allowed_values" in value:
        import capo_iotfleetwise.types.list_of_strings

        out["allowedValues"] = (
            capo_iotfleetwise.types.list_of_strings.serialize_aws_json_1_0(
                value["allowed_values"]
            )
        )
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    if "deprecation_message" in value:
        out["deprecationMessage"] = value["deprecation_message"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "struct_fully_qualified_name" in value:
        out["structFullyQualifiedName"] = value["struct_fully_qualified_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Sensor:
    out: Sensor = {}  # type: ignore[typeddict-item]
    if "fullyQualifiedName" in data:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError("Sensor.fully_qualified_name required")
    if "dataType" in data:
        import capo_iotfleetwise.types.node_data_type

        out["data_type"] = (
            capo_iotfleetwise.types.node_data_type.deserialize_aws_json_1_0(
                data["dataType"]
            )
        )
    else:
        raise DeserializationError("Sensor.data_type required")
    if "description" in data:
        out["description"] = data["description"]
    if "unit" in data:
        out["unit"] = data["unit"]
    if "allowedValues" in data:
        import capo_iotfleetwise.types.list_of_strings

        out["allowed_values"] = (
            capo_iotfleetwise.types.list_of_strings.deserialize_aws_json_1_0(
                data["allowedValues"]
            )
        )
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    if "deprecationMessage" in data:
        out["deprecation_message"] = data["deprecationMessage"]
    if "comment" in data:
        out["comment"] = data["comment"]
    if "structFullyQualifiedName" in data:
        out["struct_fully_qualified_name"] = data["structFullyQualifiedName"]
    return out
