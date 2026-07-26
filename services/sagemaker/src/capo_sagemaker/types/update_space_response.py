"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.space_arn


class UpdateSpaceResponse(TypedDict, closed=True):
    space_arn: NotRequired["capo_sagemaker.types.space_arn.SpaceArn"]
    """<p>The space's Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSpaceResponse) -> dict:
    out: dict = {}
    if "space_arn" in value:
        out["SpaceArn"] = value["space_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSpaceResponse:
    out: UpdateSpaceResponse = {}  # type: ignore[typeddict-item]
    if "SpaceArn" in data:
        out["space_arn"] = data["SpaceArn"]
    return out
