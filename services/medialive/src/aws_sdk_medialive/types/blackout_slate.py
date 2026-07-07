"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min34_max34
    import aws_sdk_medialive.types.blackout_slate_network_end_blackout
    import aws_sdk_medialive.types.blackout_slate_state
    import aws_sdk_medialive.types.input_location


class BlackoutSlate(TypedDict, closed=True):
    blackout_slate_image: NotRequired[
        "aws_sdk_medialive.types.input_location.InputLocation"
    ]
    """Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported."""
    network_end_blackout: NotRequired[
        "aws_sdk_medialive.types.blackout_slate_network_end_blackout.BlackoutSlateNetworkEndBlackout"
    ]
    r"""Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the \"Network Blackout Image\" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in \"Network ID\"."""
    network_end_blackout_image: NotRequired[
        "aws_sdk_medialive.types.input_location.InputLocation"
    ]
    """Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster."""
    network_id: NotRequired[
        "aws_sdk_medialive.types.__string_min34_max34.__stringMin34Max34"
    ]
    r"""Provides Network ID that matches EIDR ID format (e.g., \"10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C\")."""
    state: NotRequired[
        "aws_sdk_medialive.types.blackout_slate_state.BlackoutSlateState"
    ]
    """When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata."""


# --- restJson1 ser/de ---
def serialize_json(value: BlackoutSlate) -> dict:
    out: dict = {}
    if "blackout_slate_image" in value:
        import aws_sdk_medialive.types.input_location

        out["blackoutSlateImage"] = (
            aws_sdk_medialive.types.input_location.serialize_json(
                value["blackout_slate_image"]
            )
        )
    if "network_end_blackout" in value:
        import aws_sdk_medialive.types.blackout_slate_network_end_blackout

        out["networkEndBlackout"] = (
            aws_sdk_medialive.types.blackout_slate_network_end_blackout.serialize_json(
                value["network_end_blackout"]
            )
        )
    if "network_end_blackout_image" in value:
        import aws_sdk_medialive.types.input_location

        out["networkEndBlackoutImage"] = (
            aws_sdk_medialive.types.input_location.serialize_json(
                value["network_end_blackout_image"]
            )
        )
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "state" in value:
        import aws_sdk_medialive.types.blackout_slate_state

        out["state"] = aws_sdk_medialive.types.blackout_slate_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> BlackoutSlate:
    out: BlackoutSlate = {}  # type: ignore[typeddict-item]
    if "blackoutSlateImage" in data:
        import aws_sdk_medialive.types.input_location

        out["blackout_slate_image"] = (
            aws_sdk_medialive.types.input_location.deserialize_json(
                data["blackoutSlateImage"]
            )
        )
    if "networkEndBlackout" in data:
        import aws_sdk_medialive.types.blackout_slate_network_end_blackout

        out["network_end_blackout"] = (
            aws_sdk_medialive.types.blackout_slate_network_end_blackout.deserialize_json(
                data["networkEndBlackout"]
            )
        )
    if "networkEndBlackoutImage" in data:
        import aws_sdk_medialive.types.input_location

        out["network_end_blackout_image"] = (
            aws_sdk_medialive.types.input_location.deserialize_json(
                data["networkEndBlackoutImage"]
            )
        )
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    if "state" in data:
        import aws_sdk_medialive.types.blackout_slate_state

        out["state"] = aws_sdk_medialive.types.blackout_slate_state.deserialize_json(
            data["state"]
        )
    return out
