"""Generated from Smithy shape ``com.amazonaws.rekognition#ValidationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.assets


class ValidationData(TypedDict, closed=True):
    assets: NotRequired["capo_rekognition.types.assets.Assets"]
    """<p>The assets that comprise the validation data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationData) -> dict:
    out: dict = {}
    if "assets" in value:
        import capo_rekognition.types.assets

        out["Assets"] = capo_rekognition.types.assets.serialize_aws_json_1_1(
            value["assets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationData:
    out: ValidationData = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import capo_rekognition.types.assets

        out["assets"] = capo_rekognition.types.assets.deserialize_aws_json_1_1(
            data["Assets"]
        )
    return out
