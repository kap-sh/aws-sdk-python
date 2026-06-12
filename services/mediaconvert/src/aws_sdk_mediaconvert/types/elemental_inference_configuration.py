"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature
    import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed


class ElementalInferenceConfiguration(TypedDict):
    features: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature.__listOfElementalInferenceFeature"
    ]
    """A list of Elemental Inference features used in this job."""
    feeds: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed.__listOfElementalInferenceFeed"
    ]
    """A list of Elemental Inference feeds used by this job."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceConfiguration) -> dict:
    out: dict = {}
    if "features" in value:
        import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature

        out["features"] = (
            aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature.serialize_json(
                value["features"]
            )
        )
    if "feeds" in value:
        import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed

        out["feeds"] = (
            aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed.serialize_json(
                value["feeds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElementalInferenceConfiguration:
    out: ElementalInferenceConfiguration = {}  # type: ignore[typeddict-item]
    if "features" in data:
        import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature

        out["features"] = (
            aws_sdk_mediaconvert.types.__list_of_elemental_inference_feature.deserialize_json(
                data["features"]
            )
        )
    if "feeds" in data:
        import aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed

        out["feeds"] = (
            aws_sdk_mediaconvert.types.__list_of_elemental_inference_feed.deserialize_json(
                data["feeds"]
            )
        )
    return out
