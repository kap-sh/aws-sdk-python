"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.journey_run_status


class JourneyRunResponse(TypedDict):
    creation_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The time when the journey run was created or scheduled, in ISO 8601 format.</p>"""
    last_update_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The last time the journey run was updated, in ISO 8601 format..</p>"""
    run_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the run.</p>"""
    status: NotRequired["aws_sdk_pinpoint.types.journey_run_status.JourneyRunStatus"]
    """<p>The current status of the journey run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyRunResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "last_update_time" in value:
        out["LastUpdateTime"] = value["last_update_time"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "status" in value:
        import aws_sdk_pinpoint.types.journey_run_status

        out["Status"] = aws_sdk_pinpoint.types.journey_run_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> JourneyRunResponse:
    out: JourneyRunResponse = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "LastUpdateTime" in data:
        out["last_update_time"] = data["LastUpdateTime"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "Status" in data:
        import aws_sdk_pinpoint.types.journey_run_status

        out["status"] = aws_sdk_pinpoint.types.journey_run_status.deserialize_json(
            data["Status"]
        )
    return out
