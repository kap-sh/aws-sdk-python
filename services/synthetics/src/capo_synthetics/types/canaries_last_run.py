"""Generated from Smithy shape ``com.amazonaws.synthetics#CanariesLastRun``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.canary_last_run

CanariesLastRun: TypeAlias = list["capo_synthetics.types.canary_last_run.CanaryLastRun"]


# --- restJson1 ser/de ---
def serialize_json(value: CanariesLastRun) -> list:
    import capo_synthetics.types.canary_last_run

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.canary_last_run.serialize_json(item))
    return out


def deserialize_json(data: list) -> CanariesLastRun:
    import capo_synthetics.types.canary_last_run

    out: CanariesLastRun = []
    for item in data:
        out.append(capo_synthetics.types.canary_last_run.deserialize_json(item))
    return out
