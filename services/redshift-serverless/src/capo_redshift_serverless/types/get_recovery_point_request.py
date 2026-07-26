"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetRecoveryPointRequest``."""

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError


class GetRecoveryPointRequest(TypedDict, closed=True):
    recovery_point_id: "str"
    """<p>The unique identifier of the recovery point to return information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRecoveryPointRequest) -> dict:
    out: dict = {}
    out["recoveryPointId"] = value["recovery_point_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRecoveryPointRequest:
    out: GetRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    if "recoveryPointId" in data:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        raise DeserializationError("GetRecoveryPointRequest.recovery_point_id required")
    return out
