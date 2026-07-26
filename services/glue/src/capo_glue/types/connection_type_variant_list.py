"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionTypeVariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.connection_type_variant

ConnectionTypeVariantList: TypeAlias = list[
    "capo_glue.types.connection_type_variant.ConnectionTypeVariant"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionTypeVariantList) -> list:
    import capo_glue.types.connection_type_variant

    out: list = []
    for item in value:
        out.append(capo_glue.types.connection_type_variant.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionTypeVariantList:
    import capo_glue.types.connection_type_variant

    out: ConnectionTypeVariantList = []
    for item in data:
        out.append(
            capo_glue.types.connection_type_variant.deserialize_aws_json_1_1(item)
        )
    return out
