"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.connected_home_settings
    import capo_rekognition.types.face_search_settings


class StreamProcessorSettings(TypedDict, closed=True):
    face_search: NotRequired[
        "capo_rekognition.types.face_search_settings.FaceSearchSettings"
    ]
    """<p>Face search settings to use on a streaming video. </p>"""
    connected_home: NotRequired[
        "capo_rekognition.types.connected_home_settings.ConnectedHomeSettings"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorSettings) -> dict:
    out: dict = {}
    if "face_search" in value:
        import capo_rekognition.types.face_search_settings

        out["FaceSearch"] = (
            capo_rekognition.types.face_search_settings.serialize_aws_json_1_1(
                value["face_search"]
            )
        )
    if "connected_home" in value:
        import capo_rekognition.types.connected_home_settings

        out["ConnectedHome"] = (
            capo_rekognition.types.connected_home_settings.serialize_aws_json_1_1(
                value["connected_home"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorSettings:
    out: StreamProcessorSettings = {}  # type: ignore[typeddict-item]
    if "FaceSearch" in data:
        import capo_rekognition.types.face_search_settings

        out["face_search"] = (
            capo_rekognition.types.face_search_settings.deserialize_aws_json_1_1(
                data["FaceSearch"]
            )
        )
    if "ConnectedHome" in data:
        import capo_rekognition.types.connected_home_settings

        out["connected_home"] = (
            capo_rekognition.types.connected_home_settings.deserialize_aws_json_1_1(
                data["ConnectedHome"]
            )
        )
    return out
