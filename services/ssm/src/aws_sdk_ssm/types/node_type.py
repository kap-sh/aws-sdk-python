"""Generated from Smithy shape ``com.amazonaws.ssm#NodeType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_info


class _NodeType_Instance(TypedDict, closed=True):
    Instance: "aws_sdk_ssm.types.instance_info.InstanceInfo"


NodeType: TypeAlias = _NodeType_Instance


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeType) -> dict:
    if "Instance" in value:
        import aws_sdk_ssm.types.instance_info

        return {
            "Instance": aws_sdk_ssm.types.instance_info.serialize_aws_json_1_1(
                value["Instance"]
            )
        }
    else:
        raise SerializationError("NodeType: no variant present")


def deserialize_aws_json_1_1(data: dict) -> NodeType:
    if "Instance" in data:
        import aws_sdk_ssm.types.instance_info

        return {
            "Instance": aws_sdk_ssm.types.instance_info.deserialize_aws_json_1_1(
                data["Instance"]
            )
        }
    else:
        raise DeserializationError("NodeType: no recognized variant key")
