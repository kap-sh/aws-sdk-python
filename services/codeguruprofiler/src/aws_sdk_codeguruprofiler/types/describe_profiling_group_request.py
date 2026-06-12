"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#DescribeProfilingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class DescribeProfilingGroupRequest(TypedDict):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p> The name of the profiling group to get information about. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProfilingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProfilingGroupRequest:
    out: DescribeProfilingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
