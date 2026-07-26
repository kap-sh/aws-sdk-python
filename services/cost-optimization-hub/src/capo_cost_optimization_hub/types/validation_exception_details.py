"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ValidationExceptionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.validation_exception_detail

ValidationExceptionDetails: TypeAlias = list[
    "capo_cost_optimization_hub.types.validation_exception_detail.ValidationExceptionDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionDetails) -> list:
    import capo_cost_optimization_hub.types.validation_exception_detail

    out: list = []
    for item in value:
        out.append(
            capo_cost_optimization_hub.types.validation_exception_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ValidationExceptionDetails:
    import capo_cost_optimization_hub.types.validation_exception_detail

    out: ValidationExceptionDetails = []
    for item in data:
        out.append(
            capo_cost_optimization_hub.types.validation_exception_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
