"""Generated from Smithy shape ``com.amazonaws.mgn#TerminateTargetInstancesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.job


class TerminateTargetInstancesResponse(TypedDict):
    job: NotRequired["aws_sdk_mgn.types.job.Job"]
    """<p>Terminate Target instance Job response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateTargetInstancesResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_mgn.types.job

        out["job"] = aws_sdk_mgn.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> TerminateTargetInstancesResponse:
    out: TerminateTargetInstancesResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_mgn.types.job

        out["job"] = aws_sdk_mgn.types.job.deserialize_json(data["job"])
    return out
