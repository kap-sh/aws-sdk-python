"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ExtendedDataServices``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.copy_protection_action
    import aws_sdk_mediaconvert.types.vchip_action


class ExtendedDataServices(TypedDict, closed=True):
    copy_protection_action: NotRequired[
        "aws_sdk_mediaconvert.types.copy_protection_action.CopyProtectionAction"
    ]
    """The action to take on copy and redistribution control XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions."""
    vchip_action: NotRequired["aws_sdk_mediaconvert.types.vchip_action.VchipAction"]
    """The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions."""


# --- restJson1 ser/de ---
def serialize_json(value: ExtendedDataServices) -> dict:
    out: dict = {}
    if "copy_protection_action" in value:
        import aws_sdk_mediaconvert.types.copy_protection_action

        out["copyProtectionAction"] = (
            aws_sdk_mediaconvert.types.copy_protection_action.serialize_json(
                value["copy_protection_action"]
            )
        )
    if "vchip_action" in value:
        import aws_sdk_mediaconvert.types.vchip_action

        out["vchipAction"] = aws_sdk_mediaconvert.types.vchip_action.serialize_json(
            value["vchip_action"]
        )
    return out


def deserialize_json(data: dict) -> ExtendedDataServices:
    out: ExtendedDataServices = {}  # type: ignore[typeddict-item]
    if "copyProtectionAction" in data:
        import aws_sdk_mediaconvert.types.copy_protection_action

        out["copy_protection_action"] = (
            aws_sdk_mediaconvert.types.copy_protection_action.deserialize_json(
                data["copyProtectionAction"]
            )
        )
    if "vchipAction" in data:
        import aws_sdk_mediaconvert.types.vchip_action

        out["vchip_action"] = aws_sdk_mediaconvert.types.vchip_action.deserialize_json(
            data["vchipAction"]
        )
    return out
