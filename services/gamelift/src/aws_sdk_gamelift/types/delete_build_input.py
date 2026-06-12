"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteBuildInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_id_or_arn


class DeleteBuildInput(TypedDict):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to delete. You can use either the build ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBuildInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBuildInput:
    out: DeleteBuildInput = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    return out
