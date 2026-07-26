"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryLastRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_name
    import capo_synthetics.types.canary_run


class CanaryLastRun(TypedDict, closed=True):
    canary_name: NotRequired["capo_synthetics.types.canary_name.CanaryName"]
    """<p>The name of the canary.</p>"""
    last_run: NotRequired["capo_synthetics.types.canary_run.CanaryRun"]
    """<p>The results from this canary's most recent run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryLastRun) -> dict:
    out: dict = {}
    if "canary_name" in value:
        out["CanaryName"] = value["canary_name"]
    if "last_run" in value:
        import capo_synthetics.types.canary_run

        out["LastRun"] = capo_synthetics.types.canary_run.serialize_json(
            value["last_run"]
        )
    return out


def deserialize_json(data: dict) -> CanaryLastRun:
    out: CanaryLastRun = {}  # type: ignore[typeddict-item]
    if "CanaryName" in data:
        out["canary_name"] = data["CanaryName"]
    if "LastRun" in data:
        import capo_synthetics.types.canary_run

        out["last_run"] = capo_synthetics.types.canary_run.deserialize_json(
            data["LastRun"]
        )
    return out
