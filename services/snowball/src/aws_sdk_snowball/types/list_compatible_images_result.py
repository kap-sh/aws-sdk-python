"""Generated from Smithy shape ``com.amazonaws.snowball#ListCompatibleImagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.compatible_image_list
    import aws_sdk_snowball.types.string


class ListCompatibleImagesResult(TypedDict):
    compatible_images: NotRequired[
        "aws_sdk_snowball.types.compatible_image_list.CompatibleImageList"
    ]
    """<p>A JSON-formatted object that describes a compatible AMI, including the ID and name for a Snow device AMI.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Because HTTP requests are stateless, this is the starting point for your next list of returned images.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompatibleImagesResult) -> dict:
    out: dict = {}
    if "compatible_images" in value:
        import aws_sdk_snowball.types.compatible_image_list

        out["CompatibleImages"] = (
            aws_sdk_snowball.types.compatible_image_list.serialize_aws_json_1_1(
                value["compatible_images"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCompatibleImagesResult:
    out: ListCompatibleImagesResult = {}  # type: ignore[typeddict-item]
    if "CompatibleImages" in data:
        import aws_sdk_snowball.types.compatible_image_list

        out["compatible_images"] = (
            aws_sdk_snowball.types.compatible_image_list.deserialize_aws_json_1_1(
                data["CompatibleImages"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
