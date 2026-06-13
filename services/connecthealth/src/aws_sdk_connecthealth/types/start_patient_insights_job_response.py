"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartPatientInsightsJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_connecthealth.types.job_arn
    import aws_sdk_connecthealth.types.job_id


class StartPatientInsightsJobResponse(TypedDict):
    job_arn: "aws_sdk_connecthealth.types.job_arn.JobArn"
    """<p/>"""
    job_id: "aws_sdk_connecthealth.types.job_id.JobId"
    """<p/>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPatientInsightsJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobId"] = value["job_id"]
    if "creation_time" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartPatientInsightsJobResponse:
    out: StartPatientInsightsJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("StartPatientInsightsJobResponse.job_arn required")
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("StartPatientInsightsJobResponse.job_id required")
    if "creationTime" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    return out
