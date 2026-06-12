"""Generated from Smithy shape ``com.amazonaws.gamelift#RequestUploadCredentialsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_id_or_arn


class RequestUploadCredentialsInput(TypedDict):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to get credentials for. You can use either the build ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestUploadCredentialsInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestUploadCredentialsInput:
    out: RequestUploadCredentialsInput = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    return out
