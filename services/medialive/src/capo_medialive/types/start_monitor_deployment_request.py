"""Generated from Smithy shape ``com.amazonaws.medialive#StartMonitorDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__boolean
    import capo_medialive.types.__string


class StartMonitorDeploymentRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_medialive.types.__boolean.__boolean"]
    identifier: "capo_medialive.types.__string.__string"
    """A signal map's identifier. Can be either be its id or current name."""


# --- restJson1 ser/de ---
def serialize_json(value: StartMonitorDeploymentRequest) -> dict:
    out: dict = {}
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> StartMonitorDeploymentRequest:
    out: StartMonitorDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    return out
