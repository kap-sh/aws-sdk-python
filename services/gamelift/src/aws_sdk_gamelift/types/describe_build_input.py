"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeBuildInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.build_id_or_arn


class DescribeBuildInput(TypedDict):
    build_id: NotRequired["aws_sdk_gamelift.types.build_id_or_arn.BuildIdOrArn"]
    """<p>A unique identifier for the build to retrieve properties for. You can use either the build ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBuildInput) -> dict:
    out: dict = {}
    if "build_id" in value:
        out["BuildId"] = value["build_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBuildInput:
    out: DescribeBuildInput = {}  # type: ignore[typeddict-item]
    if "BuildId" in data:
        out["build_id"] = data["BuildId"]
    return out
