"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Ami``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_state
    import aws_sdk_imagebuilder.types.non_empty_string


class Ami(TypedDict):
    region: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services Region of the Amazon EC2 AMI.</p>"""
    image: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The AMI ID of the Amazon EC2 AMI.</p>"""
    name: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon EC2 AMI.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the Amazon EC2 AMI. Minimum and maximum length are in characters.</p>"""
    state: NotRequired["aws_sdk_imagebuilder.types.image_state.ImageState"]
    account_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The account ID of the owner of the AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ami) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "image" in value:
        out["image"] = value["image"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "state" in value:
        import aws_sdk_imagebuilder.types.image_state

        out["state"] = aws_sdk_imagebuilder.types.image_state.serialize_json(
            value["state"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> Ami:
    out: Ami = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "image" in data:
        out["image"] = data["image"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "state" in data:
        import aws_sdk_imagebuilder.types.image_state

        out["state"] = aws_sdk_imagebuilder.types.image_state.deserialize_json(
            data["state"]
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out
