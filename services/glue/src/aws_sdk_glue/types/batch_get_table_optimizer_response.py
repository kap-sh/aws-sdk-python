"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_get_table_optimizer_errors
    import aws_sdk_glue.types.batch_table_optimizers


class BatchGetTableOptimizerResponse(TypedDict):
    table_optimizers: NotRequired[
        "aws_sdk_glue.types.batch_table_optimizers.BatchTableOptimizers"
    ]
    """<p>A list of <code>BatchTableOptimizer</code> objects.</p>"""
    failures: NotRequired[
        "aws_sdk_glue.types.batch_get_table_optimizer_errors.BatchGetTableOptimizerErrors"
    ]
    """<p>A list of errors from the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerResponse) -> dict:
    out: dict = {}
    if "table_optimizers" in value:
        import aws_sdk_glue.types.batch_table_optimizers

        out["TableOptimizers"] = (
            aws_sdk_glue.types.batch_table_optimizers.serialize_aws_json_1_1(
                value["table_optimizers"]
            )
        )
    if "failures" in value:
        import aws_sdk_glue.types.batch_get_table_optimizer_errors

        out["Failures"] = (
            aws_sdk_glue.types.batch_get_table_optimizer_errors.serialize_aws_json_1_1(
                value["failures"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTableOptimizerResponse:
    out: BatchGetTableOptimizerResponse = {}  # type: ignore[typeddict-item]
    if "TableOptimizers" in data:
        import aws_sdk_glue.types.batch_table_optimizers

        out["table_optimizers"] = (
            aws_sdk_glue.types.batch_table_optimizers.deserialize_aws_json_1_1(
                data["TableOptimizers"]
            )
        )
    if "Failures" in data:
        import aws_sdk_glue.types.batch_get_table_optimizer_errors

        out["failures"] = (
            aws_sdk_glue.types.batch_get_table_optimizer_errors.deserialize_aws_json_1_1(
                data["Failures"]
            )
        )
    return out
