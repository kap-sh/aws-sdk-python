"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id


class DescribeEnvironmentStatusRequest(TypedDict):
    environment_id: "aws_sdk_cloud9.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to get status information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentStatusRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentStatusRequest:
    out: DescribeEnvironmentStatusRequest = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "DescribeEnvironmentStatusRequest.environment_id required"
        )
    return out
