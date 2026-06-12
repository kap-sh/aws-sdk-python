"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionTypeVariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_type_variant

ConnectionTypeVariantList: TypeAlias = list[
    "aws_sdk_glue.types.connection_type_variant.ConnectionTypeVariant"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionTypeVariantList) -> list:
    import aws_sdk_glue.types.connection_type_variant

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.connection_type_variant.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionTypeVariantList:
    import aws_sdk_glue.types.connection_type_variant

    out: ConnectionTypeVariantList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.connection_type_variant.deserialize_aws_json_1_1(item)
        )
    return out
