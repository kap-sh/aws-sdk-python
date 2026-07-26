"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2ImageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Ec2ImageDetails(TypedDict, closed=True):
    image_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the EC2 AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2ImageDetails) -> dict:
    out: dict = {}
    if "image_arn" in value:
        out["imageArn"] = value["image_arn"]
    return out


def deserialize_json(data: dict) -> Ec2ImageDetails:
    out: Ec2ImageDetails = {}  # type: ignore[typeddict-item]
    if "imageArn" in data:
        out["image_arn"] = data["imageArn"]
    return out
