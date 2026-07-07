"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image


class PutImageResponse(TypedDict, closed=True):
    image: NotRequired["aws_sdk_ecr.types.image.Image"]
    """<p>Details of the image uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageResponse) -> dict:
    out: dict = {}
    if "image" in value:
        import aws_sdk_ecr.types.image

        out["image"] = aws_sdk_ecr.types.image.serialize_aws_json_1_1(value["image"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageResponse:
    out: PutImageResponse = {}  # type: ignore[typeddict-item]
    if "image" in data:
        import aws_sdk_ecr.types.image

        out["image"] = aws_sdk_ecr.types.image.deserialize_aws_json_1_1(data["image"])
    return out
