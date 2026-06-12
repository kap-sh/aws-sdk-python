"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class GetNotificationConfigurationRequest(TypedDict):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group we want to get the notification configuration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationRequest:
    out: GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
