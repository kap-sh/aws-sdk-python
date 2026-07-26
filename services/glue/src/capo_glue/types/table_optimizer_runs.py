"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.table_optimizer_run

TableOptimizerRuns: TypeAlias = list[
    "capo_glue.types.table_optimizer_run.TableOptimizerRun"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerRuns) -> list:
    import capo_glue.types.table_optimizer_run

    out: list = []
    for item in value:
        out.append(capo_glue.types.table_optimizer_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableOptimizerRuns:
    import capo_glue.types.table_optimizer_run

    out: TableOptimizerRuns = []
    for item in data:
        out.append(capo_glue.types.table_optimizer_run.deserialize_aws_json_1_1(item))
    return out
