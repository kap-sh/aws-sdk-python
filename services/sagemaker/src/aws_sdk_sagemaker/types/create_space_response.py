"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateSpaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.space_arn


class CreateSpaceResponse(TypedDict):
    space_arn: NotRequired["aws_sdk_sagemaker.types.space_arn.SpaceArn"]
    """<p>The space's Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSpaceResponse) -> dict:
    out: dict = {}
    if "space_arn" in value:
        out["SpaceArn"] = value["space_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSpaceResponse:
    out: CreateSpaceResponse = {}  # type: ignore[typeddict-item]
    if "SpaceArn" in data:
        out["space_arn"] = data["SpaceArn"]
    return out
