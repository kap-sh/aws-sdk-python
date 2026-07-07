"""Generated from Smithy shape ``com.amazonaws.drs#TerminateRecoveryInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.job


class TerminateRecoveryInstancesResponse(TypedDict, closed=True):
    job: NotRequired["aws_sdk_drs.types.job.Job"]
    """<p>The Job for terminating the Recovery Instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateRecoveryInstancesResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_drs.types.job

        out["job"] = aws_sdk_drs.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> TerminateRecoveryInstancesResponse:
    out: TerminateRecoveryInstancesResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_drs.types.job

        out["job"] = aws_sdk_drs.types.job.deserialize_json(data["job"])
    return out
