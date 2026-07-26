"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLambdaFunctionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.exportable_lambda_function_field

ExportableLambdaFunctionFields: TypeAlias = list[
    "capo_compute_optimizer.types.exportable_lambda_function_field.ExportableLambdaFunctionField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableLambdaFunctionFields) -> list:
    import capo_compute_optimizer.types.exportable_lambda_function_field

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.exportable_lambda_function_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableLambdaFunctionFields:
    import capo_compute_optimizer.types.exportable_lambda_function_field

    out: ExportableLambdaFunctionFields = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.exportable_lambda_function_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
