"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorDataSharingPreference``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.boolean


class StreamProcessorDataSharingPreference(TypedDict):
    opt_in: "aws_sdk_rekognition.types.boolean.Boolean"
    """<p> If this option is set to true, you choose to share data with Rekognition to improve model performance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorDataSharingPreference) -> dict:
    out: dict = {}
    out["OptIn"] = value.get("opt_in", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorDataSharingPreference:
    out: StreamProcessorDataSharingPreference = {}  # type: ignore[typeddict-item]
    if "OptIn" in data:
        out["opt_in"] = data["OptIn"]
    else:
        out["opt_in"] = False
    return out
