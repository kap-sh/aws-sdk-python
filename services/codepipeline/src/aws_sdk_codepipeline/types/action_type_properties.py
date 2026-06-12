"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_type_property

ActionTypeProperties: TypeAlias = list[
    "aws_sdk_codepipeline.types.action_type_property.ActionTypeProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeProperties) -> list:
    import aws_sdk_codepipeline.types.action_type_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.action_type_property.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ActionTypeProperties:
    import aws_sdk_codepipeline.types.action_type_property

    out: ActionTypeProperties = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.action_type_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out
