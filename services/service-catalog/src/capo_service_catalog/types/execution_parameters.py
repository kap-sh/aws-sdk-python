"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecutionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.execution_parameter

ExecutionParameters: TypeAlias = list[
    "capo_service_catalog.types.execution_parameter.ExecutionParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionParameters) -> list:
    import capo_service_catalog.types.execution_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.execution_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutionParameters:
    import capo_service_catalog.types.execution_parameter

    out: ExecutionParameters = []
    for item in data:
        out.append(
            capo_service_catalog.types.execution_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
