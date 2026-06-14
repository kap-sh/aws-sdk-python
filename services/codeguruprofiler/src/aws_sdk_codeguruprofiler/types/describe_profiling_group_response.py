"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#DescribeProfilingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_description


class DescribeProfilingGroupResponse(TypedDict):
    profiling_group: "aws_sdk_codeguruprofiler.types.profiling_group_description.ProfilingGroupDescription"
    r"""<p> The returned <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\"> <code>ProfilingGroupDescription</code> </a> object that contains information about the requested profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProfilingGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.profiling_group_description

    out["profilingGroup"] = (
        aws_sdk_codeguruprofiler.types.profiling_group_description.serialize_json(
            value["profiling_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeProfilingGroupResponse:
    out: DescribeProfilingGroupResponse = {}  # type: ignore[typeddict-item]
    if "profilingGroup" in data:
        import aws_sdk_codeguruprofiler.types.profiling_group_description

        out["profiling_group"] = (
            aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
                data["profilingGroup"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProfilingGroupResponse.profiling_group required"
        )
    return out
