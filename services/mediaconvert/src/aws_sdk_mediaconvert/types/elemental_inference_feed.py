"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.elemental_inference_feed_management_state


class ElementalInferenceFeed(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Feed ARN."""
    feed_management_state: NotRequired[
        "aws_sdk_mediaconvert.types.elemental_inference_feed_management_state.ElementalInferenceFeedManagementState"
    ]
    """Elemental Inference Feed management state."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceFeed) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "feed_management_state" in value:
        import aws_sdk_mediaconvert.types.elemental_inference_feed_management_state

        out["feedManagementState"] = (
            aws_sdk_mediaconvert.types.elemental_inference_feed_management_state.serialize_json(
                value["feed_management_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElementalInferenceFeed:
    out: ElementalInferenceFeed = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "feedManagementState" in data:
        import aws_sdk_mediaconvert.types.elemental_inference_feed_management_state

        out["feed_management_state"] = (
            aws_sdk_mediaconvert.types.elemental_inference_feed_management_state.deserialize_json(
                data["feedManagementState"]
            )
        )
    return out
