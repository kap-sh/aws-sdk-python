"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UpdateProfilingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_description


class UpdateProfilingGroupResponse(TypedDict):
    profiling_group: "aws_sdk_codeguruprofiler.types.profiling_group_description.ProfilingGroupDescription"
    """<p> A <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html\"> <code>ProfilingGroupDescription</code> </a> that contains information about the returned updated profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfilingGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.profiling_group_description

    out["profilingGroup"] = (
        aws_sdk_codeguruprofiler.types.profiling_group_description.serialize_json(
            value["profiling_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProfilingGroupResponse:
    out: UpdateProfilingGroupResponse = {}  # type: ignore[typeddict-item]
    if "profilingGroup" in data:
        import aws_sdk_codeguruprofiler.types.profiling_group_description

        out["profiling_group"] = (
            aws_sdk_codeguruprofiler.types.profiling_group_description.deserialize_json(
                data["profilingGroup"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfilingGroupResponse.profiling_group required"
        )
    return out
