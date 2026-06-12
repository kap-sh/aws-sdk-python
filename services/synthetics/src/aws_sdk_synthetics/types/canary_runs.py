"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canary_run

CanaryRuns: TypeAlias = list["aws_sdk_synthetics.types.canary_run.CanaryRun"]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRuns) -> list:
    import aws_sdk_synthetics.types.canary_run

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.canary_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> CanaryRuns:
    import aws_sdk_synthetics.types.canary_run

    out: CanaryRuns = []
    for item in data:
        out.append(aws_sdk_synthetics.types.canary_run.deserialize_json(item))
    return out
