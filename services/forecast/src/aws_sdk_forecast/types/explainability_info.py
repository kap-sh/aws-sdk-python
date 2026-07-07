"""Generated from Smithy shape ``com.amazonaws.forecast#ExplainabilityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.status


class ExplainabilityInfo(TypedDict, closed=True):
    explainability_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the Explainability. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainabilityInfo) -> dict:
    out: dict = {}
    if "explainability_arn" in value:
        out["ExplainabilityArn"] = value["explainability_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExplainabilityInfo:
    out: ExplainabilityInfo = {}  # type: ignore[typeddict-item]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
