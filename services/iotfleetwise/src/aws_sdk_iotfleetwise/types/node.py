"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Node``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.actuator
    import aws_sdk_iotfleetwise.types.attribute
    import aws_sdk_iotfleetwise.types.branch
    import aws_sdk_iotfleetwise.types.custom_property
    import aws_sdk_iotfleetwise.types.custom_struct
    import aws_sdk_iotfleetwise.types.sensor


class _Node_branch(TypedDict, closed=True):
    branch: "aws_sdk_iotfleetwise.types.branch.Branch"


class _Node_sensor(TypedDict, closed=True):
    sensor: "aws_sdk_iotfleetwise.types.sensor.Sensor"


class _Node_actuator(TypedDict, closed=True):
    actuator: "aws_sdk_iotfleetwise.types.actuator.Actuator"


class _Node_attribute(TypedDict, closed=True):
    attribute: "aws_sdk_iotfleetwise.types.attribute.Attribute"


class _Node_struct(TypedDict, closed=True):
    struct: "aws_sdk_iotfleetwise.types.custom_struct.CustomStruct"


class _Node_property(TypedDict, closed=True):
    property: "aws_sdk_iotfleetwise.types.custom_property.CustomProperty"


Node: TypeAlias = (
    _Node_branch
    | _Node_sensor
    | _Node_actuator
    | _Node_attribute
    | _Node_struct
    | _Node_property
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Node) -> dict:
    if "branch" in value:
        import aws_sdk_iotfleetwise.types.branch

        return {
            "branch": aws_sdk_iotfleetwise.types.branch.serialize_aws_json_1_0(
                value["branch"]
            )
        }
    elif "sensor" in value:
        import aws_sdk_iotfleetwise.types.sensor

        return {
            "sensor": aws_sdk_iotfleetwise.types.sensor.serialize_aws_json_1_0(
                value["sensor"]
            )
        }
    elif "actuator" in value:
        import aws_sdk_iotfleetwise.types.actuator

        return {
            "actuator": aws_sdk_iotfleetwise.types.actuator.serialize_aws_json_1_0(
                value["actuator"]
            )
        }
    elif "attribute" in value:
        import aws_sdk_iotfleetwise.types.attribute

        return {
            "attribute": aws_sdk_iotfleetwise.types.attribute.serialize_aws_json_1_0(
                value["attribute"]
            )
        }
    elif "struct" in value:
        import aws_sdk_iotfleetwise.types.custom_struct

        return {
            "struct": aws_sdk_iotfleetwise.types.custom_struct.serialize_aws_json_1_0(
                value["struct"]
            )
        }
    elif "property" in value:
        import aws_sdk_iotfleetwise.types.custom_property

        return {
            "property": aws_sdk_iotfleetwise.types.custom_property.serialize_aws_json_1_0(
                value["property"]
            )
        }
    else:
        raise SerializationError("Node: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Node:
    if "branch" in data:
        import aws_sdk_iotfleetwise.types.branch

        return {
            "branch": aws_sdk_iotfleetwise.types.branch.deserialize_aws_json_1_0(
                data["branch"]
            )
        }
    elif "sensor" in data:
        import aws_sdk_iotfleetwise.types.sensor

        return {
            "sensor": aws_sdk_iotfleetwise.types.sensor.deserialize_aws_json_1_0(
                data["sensor"]
            )
        }
    elif "actuator" in data:
        import aws_sdk_iotfleetwise.types.actuator

        return {
            "actuator": aws_sdk_iotfleetwise.types.actuator.deserialize_aws_json_1_0(
                data["actuator"]
            )
        }
    elif "attribute" in data:
        import aws_sdk_iotfleetwise.types.attribute

        return {
            "attribute": aws_sdk_iotfleetwise.types.attribute.deserialize_aws_json_1_0(
                data["attribute"]
            )
        }
    elif "struct" in data:
        import aws_sdk_iotfleetwise.types.custom_struct

        return {
            "struct": aws_sdk_iotfleetwise.types.custom_struct.deserialize_aws_json_1_0(
                data["struct"]
            )
        }
    elif "property" in data:
        import aws_sdk_iotfleetwise.types.custom_property

        return {
            "property": aws_sdk_iotfleetwise.types.custom_property.deserialize_aws_json_1_0(
                data["property"]
            )
        }
    else:
        raise DeserializationError("Node: no recognized variant key")
