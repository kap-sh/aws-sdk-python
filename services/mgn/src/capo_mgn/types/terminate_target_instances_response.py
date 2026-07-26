"""Generated from Smithy shape ``com.amazonaws.mgn#TerminateTargetInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.job


class TerminateTargetInstancesResponse(TypedDict, closed=True):
    job: NotRequired["capo_mgn.types.job.Job"]
    """<p>Terminate Target instance Job response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateTargetInstancesResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> TerminateTargetInstancesResponse:
    out: TerminateTargetInstancesResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import capo_mgn.types.job

        out["job"] = capo_mgn.types.job.deserialize_json(data["job"])
    return out
