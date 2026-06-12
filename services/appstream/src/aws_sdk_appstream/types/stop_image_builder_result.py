"""Generated from Smithy shape ``com.amazonaws.appstream#StopImageBuilderResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.image_builder


class StopImageBuilderResult(TypedDict):
    image_builder: NotRequired["aws_sdk_appstream.types.image_builder.ImageBuilder"]
    """<p>Information about the image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopImageBuilderResult) -> dict:
    out: dict = {}
    if "image_builder" in value:
        import aws_sdk_appstream.types.image_builder

        out["ImageBuilder"] = (
            aws_sdk_appstream.types.image_builder.serialize_aws_json_1_1(
                value["image_builder"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopImageBuilderResult:
    out: StopImageBuilderResult = {}  # type: ignore[typeddict-item]
    if "ImageBuilder" in data:
        import aws_sdk_appstream.types.image_builder

        out["image_builder"] = (
            aws_sdk_appstream.types.image_builder.deserialize_aws_json_1_1(
                data["ImageBuilder"]
            )
        )
    return out
