"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeleteTestGridProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_farm_arn


class DeleteTestGridProjectRequest(TypedDict, closed=True):
    project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The ARN of the project to delete, from <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTestGridProjectRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTestGridProjectRequest:
    out: DeleteTestGridProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("DeleteTestGridProjectRequest.project_arn required")
    return out
