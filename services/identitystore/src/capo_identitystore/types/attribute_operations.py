"""Generated from Smithy shape ``com.amazonaws.identitystore#AttributeOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.attribute_operation

AttributeOperations: TypeAlias = list[
    "capo_identitystore.types.attribute_operation.AttributeOperation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeOperations) -> list:
    import capo_identitystore.types.attribute_operation

    out: list = []
    for item in value:
        out.append(
            capo_identitystore.types.attribute_operation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeOperations:
    import capo_identitystore.types.attribute_operation

    out: AttributeOperations = []
    for item in data:
        out.append(
            capo_identitystore.types.attribute_operation.deserialize_aws_json_1_1(item)
        )
    return out
