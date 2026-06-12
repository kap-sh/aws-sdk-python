"""Generated from Smithy shape ``com.amazonaws.glue#BlueprintRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_run

BlueprintRuns: TypeAlias = list["aws_sdk_glue.types.blueprint_run.BlueprintRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueprintRuns) -> list:
    import aws_sdk_glue.types.blueprint_run

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.blueprint_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BlueprintRuns:
    import aws_sdk_glue.types.blueprint_run

    out: BlueprintRuns = []
    for item in data:
        out.append(aws_sdk_glue.types.blueprint_run.deserialize_aws_json_1_1(item))
    return out
