"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestGridSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.resource_id


class GetTestGridSessionRequest(TypedDict, closed=True):
    project_arn: NotRequired["aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"]
    """<p>The ARN for the project that this session belongs to. See <a>CreateTestGridProject</a> and <a>ListTestGridProjects</a>.</p>"""
    session_id: NotRequired["aws_sdk_device_farm.types.resource_id.ResourceId"]
    """<p>An ID associated with this session.</p>"""
    session_arn: NotRequired["aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"]
    """<p>An ARN that uniquely identifies a <a>TestGridSession</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestGridSessionRequest) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["projectArn"] = value["project_arn"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "session_arn" in value:
        out["sessionArn"] = value["session_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestGridSessionRequest:
    out: GetTestGridSessionRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    return out
