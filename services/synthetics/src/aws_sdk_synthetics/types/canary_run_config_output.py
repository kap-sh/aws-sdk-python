"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.ephemeral_storage_size
    import aws_sdk_synthetics.types.max_fifteen_minutes_in_seconds
    import aws_sdk_synthetics.types.max_size3008
    import aws_sdk_synthetics.types.nullable_boolean


class CanaryRunConfigOutput(TypedDict):
    timeout_in_seconds: NotRequired[
        "aws_sdk_synthetics.types.max_fifteen_minutes_in_seconds.MaxFifteenMinutesInSeconds"
    ]
    """<p>How long the canary is allowed to run before it must stop.</p>"""
    memory_in_mb: NotRequired["aws_sdk_synthetics.types.max_size3008.MaxSize3008"]
    """<p>The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.</p>"""
    active_tracing: NotRequired[
        "aws_sdk_synthetics.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Displays whether this canary run used active X-Ray tracing. </p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_synthetics.types.ephemeral_storage_size.EphemeralStorageSize"
    ]
    """<p>Specifies the amount of ephemeral storage (in MB) to allocate for the canary run during execution. This temporary storage is used for storing canary run artifacts (which are uploaded to an Amazon S3 bucket at the end of the run), and any canary browser operations. This temporary storage is cleared after the run is completed. Default storage value is 1024 MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunConfigOutput) -> dict:
    out: dict = {}
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    if "memory_in_mb" in value:
        out["MemoryInMB"] = value["memory_in_mb"]
    if "active_tracing" in value:
        out["ActiveTracing"] = value["active_tracing"]
    if "ephemeral_storage" in value:
        out["EphemeralStorage"] = value["ephemeral_storage"]
    return out


def deserialize_json(data: dict) -> CanaryRunConfigOutput:
    out: CanaryRunConfigOutput = {}  # type: ignore[typeddict-item]
    if "TimeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    if "MemoryInMB" in data:
        out["memory_in_mb"] = data["MemoryInMB"]
    if "ActiveTracing" in data:
        out["active_tracing"] = data["ActiveTracing"]
    if "EphemeralStorage" in data:
        out["ephemeral_storage"] = data["EphemeralStorage"]
    return out
