"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ParallelExecutionBlockConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.steps


class ParallelExecutionBlockConfiguration(TypedDict):
    steps: "aws_sdk_arc_region_switch.types.steps.Steps"
    """<p>The steps for a parallel execution block.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParallelExecutionBlockConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_arc_region_switch.types.steps

    out["steps"] = aws_sdk_arc_region_switch.types.steps.serialize_aws_json_1_0(
        value["steps"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ParallelExecutionBlockConfiguration:
    out: ParallelExecutionBlockConfiguration = {}  # type: ignore[typeddict-item]
    if "steps" in data:
        import aws_sdk_arc_region_switch.types.steps

        out["steps"] = aws_sdk_arc_region_switch.types.steps.deserialize_aws_json_1_0(
            data["steps"]
        )
    else:
        raise DeserializationError("ParallelExecutionBlockConfiguration.steps required")
    return out
