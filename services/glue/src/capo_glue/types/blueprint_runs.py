"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.blueprint_run

BlueprintRuns: TypeAlias = list["capo_glue.types.blueprint_run.BlueprintRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintRuns) -> list:
    import capo_glue.types.blueprint_run

    out: list = []
    for item in value:
        out.append(capo_glue.types.blueprint_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BlueprintRuns:
    import capo_glue.types.blueprint_run

    out: BlueprintRuns = []
    for item in data:
        out.append(capo_glue.types.blueprint_run.deserialize_aws_json_1_1(item))
    return out
