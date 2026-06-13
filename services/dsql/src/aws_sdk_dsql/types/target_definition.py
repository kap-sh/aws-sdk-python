"""Generated from Smithy shape ``com.amazonaws.dsql#TargetDefinition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_dsql.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.kinesis_target_definition


class _TargetDefinition_kinesis(TypedDict):
    kinesis: "aws_sdk_dsql.types.kinesis_target_definition.KinesisTargetDefinition"


TargetDefinition: TypeAlias = _TargetDefinition_kinesis


# --- restJson1 ser/de ---
def serialize_json(value: TargetDefinition) -> dict:
    if "kinesis" in value:
        import aws_sdk_dsql.types.kinesis_target_definition

        return {
            "kinesis": aws_sdk_dsql.types.kinesis_target_definition.serialize_json(
                value["kinesis"]
            )
        }
    else:
        raise SerializationError("TargetDefinition: no variant present")


def deserialize_json(data: dict) -> TargetDefinition:
    if "kinesis" in data:
        import aws_sdk_dsql.types.kinesis_target_definition

        return {
            "kinesis": aws_sdk_dsql.types.kinesis_target_definition.deserialize_json(
                data["kinesis"]
            )
        }
    else:
        raise DeserializationError("TargetDefinition: no recognized variant key")
