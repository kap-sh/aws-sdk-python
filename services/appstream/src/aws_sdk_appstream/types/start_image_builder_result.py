"""Generated from Smithy shape ``com.amazonaws.appstream#StartImageBuilderResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.image_builder


class StartImageBuilderResult(TypedDict, closed=True):
    image_builder: NotRequired["aws_sdk_appstream.types.image_builder.ImageBuilder"]
    """<p>Information about the image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImageBuilderResult) -> dict:
    out: dict = {}
    if "image_builder" in value:
        import aws_sdk_appstream.types.image_builder

        out["ImageBuilder"] = (
            aws_sdk_appstream.types.image_builder.serialize_aws_json_1_1(
                value["image_builder"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImageBuilderResult:
    out: StartImageBuilderResult = {}  # type: ignore[typeddict-item]
    if "ImageBuilder" in data:
        import aws_sdk_appstream.types.image_builder

        out["image_builder"] = (
            aws_sdk_appstream.types.image_builder.deserialize_aws_json_1_1(
                data["ImageBuilder"]
            )
        )
    return out
