"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartFailureModeAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.client_token


class StartFailureModeAssessmentRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: StartFailureModeAssessmentRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartFailureModeAssessmentRequest:
    out: StartFailureModeAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "StartFailureModeAssessmentRequest.service_arn required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
