"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OperationsListInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.operation

OperationsListInput: TypeAlias = list[
    "aws_sdk_sagemaker_geospatial.types.operation.Operation"
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationsListInput) -> list:
    import aws_sdk_sagemaker_geospatial.types.operation

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationsListInput:
    import aws_sdk_sagemaker_geospatial.types.operation

    out: OperationsListInput = []
    for item in data:
        out.append(aws_sdk_sagemaker_geospatial.types.operation.deserialize_json(item))
    return out
