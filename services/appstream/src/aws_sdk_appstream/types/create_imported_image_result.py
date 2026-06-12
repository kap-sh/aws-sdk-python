"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImportedImageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.image


class CreateImportedImageResult(TypedDict):
    image: NotRequired["aws_sdk_appstream.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportedImageResult) -> dict:
    out: dict = {}
    if "image" in value:
        import aws_sdk_appstream.types.image

        out["Image"] = aws_sdk_appstream.types.image.serialize_aws_json_1_1(
            value["image"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportedImageResult:
    out: CreateImportedImageResult = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        import aws_sdk_appstream.types.image

        out["image"] = aws_sdk_appstream.types.image.deserialize_aws_json_1_1(
            data["Image"]
        )
    return out
