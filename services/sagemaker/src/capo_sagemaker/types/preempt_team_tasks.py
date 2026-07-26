"""Generated from Smithy shape ``com.amazonaws.sagemaker#PreemptTeamTasks``."""

from typing import Literal, TypeAlias, cast

PreemptTeamTasks: TypeAlias = Literal[
    "Never",
    "LowerPriority",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreemptTeamTasks) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreemptTeamTasks:
    return cast(PreemptTeamTasks, data)
