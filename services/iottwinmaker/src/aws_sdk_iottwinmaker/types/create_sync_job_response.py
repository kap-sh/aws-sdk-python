"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSyncJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.sync_job_state
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.twin_maker_arn


class CreateSyncJobResponse(TypedDict):
    arn: "aws_sdk_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The SyncJob ARN.</p>"""
    creation_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time for the SyncJob creation.</p>"""
    state: "aws_sdk_iottwinmaker.types.sync_job_state.SyncJobState"
    """<p>The SyncJob response state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSyncJobResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["creationDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> CreateSyncJobResponse:
    out: CreateSyncJobResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSyncJobResponse.arn required")
    if "creationDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    else:
        raise DeserializationError("CreateSyncJobResponse.creation_date_time required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("CreateSyncJobResponse.state required")
    return out
