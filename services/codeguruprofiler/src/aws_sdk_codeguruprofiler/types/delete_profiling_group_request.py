"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#DeleteProfilingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class DeleteProfilingGroupRequest(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfilingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProfilingGroupRequest:
    out: DeleteProfilingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
