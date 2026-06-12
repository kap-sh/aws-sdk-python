"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.stack_instance

StackInstances: TypeAlias = list[
    "aws_sdk_service_catalog.types.stack_instance.StackInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackInstances) -> list:
    import aws_sdk_service_catalog.types.stack_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.stack_instance.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StackInstances:
    import aws_sdk_service_catalog.types.stack_instance

    out: StackInstances = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.stack_instance.deserialize_aws_json_1_1(item)
        )
    return out
