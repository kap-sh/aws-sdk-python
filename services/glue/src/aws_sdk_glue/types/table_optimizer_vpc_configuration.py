"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerVpcConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_connection_name_string


class _TableOptimizerVpcConfiguration_glueConnectionName(TypedDict, closed=True):
    glueConnectionName: (
        "aws_sdk_glue.types.glue_connection_name_string.glueConnectionNameString"
    )


TableOptimizerVpcConfiguration: TypeAlias = (
    _TableOptimizerVpcConfiguration_glueConnectionName
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerVpcConfiguration) -> dict:
    if "glueConnectionName" in value:
        return {"glueConnectionName": value["glueConnectionName"]}
    else:
        raise SerializationError("TableOptimizerVpcConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TableOptimizerVpcConfiguration:
    if "glueConnectionName" in data:
        return {"glueConnectionName": data["glueConnectionName"]}
    else:
        raise DeserializationError(
            "TableOptimizerVpcConfiguration: no recognized variant key"
        )
