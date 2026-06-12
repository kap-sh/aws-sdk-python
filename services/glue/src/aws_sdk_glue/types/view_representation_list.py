"""Generated from Smithy shape ``com.amazonaws.glue#ViewRepresentationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.view_representation

ViewRepresentationList: TypeAlias = list[
    "aws_sdk_glue.types.view_representation.ViewRepresentation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewRepresentationList) -> list:
    import aws_sdk_glue.types.view_representation

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.view_representation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ViewRepresentationList:
    import aws_sdk_glue.types.view_representation

    out: ViewRepresentationList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.view_representation.deserialize_aws_json_1_1(item)
        )
    return out
