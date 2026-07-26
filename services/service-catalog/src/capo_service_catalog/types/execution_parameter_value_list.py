"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecutionParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.execution_parameter_value

ExecutionParameterValueList: TypeAlias = list[
    "capo_service_catalog.types.execution_parameter_value.ExecutionParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionParameterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExecutionParameterValueList:
    return list(data)
