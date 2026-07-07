"""Generated from Smithy shape ``com.amazonaws.cloud9#CreateEnvironmentEC2Result``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_id


class CreateEnvironmentEC2Result(TypedDict, closed=True):
    environment_id: NotRequired["aws_sdk_cloud9.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEnvironmentEC2Result) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEnvironmentEC2Result:
    out: CreateEnvironmentEC2Result = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    return out
