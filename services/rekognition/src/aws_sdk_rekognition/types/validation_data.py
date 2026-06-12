"""Generated from Smithy shape ``com.amazonaws.rekognition#ValidationData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.assets


class ValidationData(TypedDict):
    assets: NotRequired["aws_sdk_rekognition.types.assets.Assets"]
    """<p>The assets that comprise the validation data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationData) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_rekognition.types.assets

        out["Assets"] = aws_sdk_rekognition.types.assets.serialize_aws_json_1_1(
            value["assets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationData:
    out: ValidationData = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import aws_sdk_rekognition.types.assets

        out["assets"] = aws_sdk_rekognition.types.assets.deserialize_aws_json_1_1(
            data["Assets"]
        )
    return out
