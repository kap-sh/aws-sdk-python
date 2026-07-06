"""Generated from Smithy shape ``com.amazonaws.rekognition#TestingData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.assets
    import aws_sdk_rekognition.types.boolean


class TestingData(TypedDict, closed=True):
    assets: NotRequired["aws_sdk_rekognition.types.assets.Assets"]
    """<p>The assets used for testing.</p>"""
    auto_create: "aws_sdk_rekognition.types.boolean.Boolean"
    """<p>If specified, Rekognition splits training dataset to create a test dataset for the training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestingData) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_rekognition.types.assets

        out["Assets"] = aws_sdk_rekognition.types.assets.serialize_aws_json_1_1(
            value["assets"]
        )
    out["AutoCreate"] = value.get("auto_create", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> TestingData:
    out: TestingData = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import aws_sdk_rekognition.types.assets

        out["assets"] = aws_sdk_rekognition.types.assets.deserialize_aws_json_1_1(
            data["Assets"]
        )
    if "AutoCreate" in data:
        out["auto_create"] = data["AutoCreate"]
    else:
        out["auto_create"] = False
    return out
