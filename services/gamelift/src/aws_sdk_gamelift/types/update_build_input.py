"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateBuildInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_id_or_arn
    import aws_sdk_gamelift.types.non_zero_and_max_string


class UpdateBuildInput(TypedDict, closed=True):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to update. You can use either the build ID or ARN value. </p>"""
    name: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A descriptive label that is associated with a build. Build names do not need to be unique. </p>"""
    version: NotRequired[
        "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBuildInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBuildInput:
    out: UpdateBuildInput = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
