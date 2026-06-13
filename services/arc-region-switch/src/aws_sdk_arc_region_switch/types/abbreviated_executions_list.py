"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AbbreviatedExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.abbreviated_execution

AbbreviatedExecutionsList: TypeAlias = list[
    "aws_sdk_arc_region_switch.types.abbreviated_execution.AbbreviatedExecution"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AbbreviatedExecutionsList) -> list:
    import aws_sdk_arc_region_switch.types.abbreviated_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.abbreviated_execution.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AbbreviatedExecutionsList:
    import aws_sdk_arc_region_switch.types.abbreviated_execution

    out: AbbreviatedExecutionsList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.abbreviated_execution.deserialize_aws_json_1_0(
                item
            )
        )
    return out
