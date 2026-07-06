"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.batch_get_worker_error_code
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.worker_id


class BatchGetWorkerError(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the worker that could not be retrieved.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker that could not be retrieved.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID of the worker that could not be retrieved.</p>"""
    code: "aws_sdk_deadline.types.batch_get_worker_error_code.BatchGetWorkerErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_deadline.types.string.String"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerError) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    import aws_sdk_deadline.types.batch_get_worker_error_code

    out["code"] = aws_sdk_deadline.types.batch_get_worker_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetWorkerError:
    out: BatchGetWorkerError = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("BatchGetWorkerError.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("BatchGetWorkerError.fleet_id required")
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("BatchGetWorkerError.worker_id required")
    if "code" in data:
        import aws_sdk_deadline.types.batch_get_worker_error_code

        out["code"] = (
            aws_sdk_deadline.types.batch_get_worker_error_code.deserialize_json(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchGetWorkerError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetWorkerError.message required")
    return out
