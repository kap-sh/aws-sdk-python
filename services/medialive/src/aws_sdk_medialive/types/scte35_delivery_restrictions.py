"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35DeliveryRestrictions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.scte35_archive_allowed_flag
    import aws_sdk_medialive.types.scte35_device_restrictions
    import aws_sdk_medialive.types.scte35_no_regional_blackout_flag
    import aws_sdk_medialive.types.scte35_web_delivery_allowed_flag


class Scte35DeliveryRestrictions(TypedDict):
    archive_allowed_flag: NotRequired[
        "aws_sdk_medialive.types.scte35_archive_allowed_flag.Scte35ArchiveAllowedFlag"
    ]
    """Corresponds to SCTE-35 archive_allowed_flag."""
    device_restrictions: NotRequired[
        "aws_sdk_medialive.types.scte35_device_restrictions.Scte35DeviceRestrictions"
    ]
    """Corresponds to SCTE-35 device_restrictions parameter."""
    no_regional_blackout_flag: NotRequired[
        "aws_sdk_medialive.types.scte35_no_regional_blackout_flag.Scte35NoRegionalBlackoutFlag"
    ]
    """Corresponds to SCTE-35 no_regional_blackout_flag parameter."""
    web_delivery_allowed_flag: NotRequired[
        "aws_sdk_medialive.types.scte35_web_delivery_allowed_flag.Scte35WebDeliveryAllowedFlag"
    ]
    """Corresponds to SCTE-35 web_delivery_allowed_flag parameter."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35DeliveryRestrictions) -> dict:
    out: dict = {}
    if "archive_allowed_flag" in value:
        import aws_sdk_medialive.types.scte35_archive_allowed_flag

        out["archiveAllowedFlag"] = (
            aws_sdk_medialive.types.scte35_archive_allowed_flag.serialize_json(
                value["archive_allowed_flag"]
            )
        )
    if "device_restrictions" in value:
        import aws_sdk_medialive.types.scte35_device_restrictions

        out["deviceRestrictions"] = (
            aws_sdk_medialive.types.scte35_device_restrictions.serialize_json(
                value["device_restrictions"]
            )
        )
    if "no_regional_blackout_flag" in value:
        import aws_sdk_medialive.types.scte35_no_regional_blackout_flag

        out["noRegionalBlackoutFlag"] = (
            aws_sdk_medialive.types.scte35_no_regional_blackout_flag.serialize_json(
                value["no_regional_blackout_flag"]
            )
        )
    if "web_delivery_allowed_flag" in value:
        import aws_sdk_medialive.types.scte35_web_delivery_allowed_flag

        out["webDeliveryAllowedFlag"] = (
            aws_sdk_medialive.types.scte35_web_delivery_allowed_flag.serialize_json(
                value["web_delivery_allowed_flag"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35DeliveryRestrictions:
    out: Scte35DeliveryRestrictions = {}  # type: ignore[typeddict-item]
    if "archiveAllowedFlag" in data:
        import aws_sdk_medialive.types.scte35_archive_allowed_flag

        out["archive_allowed_flag"] = (
            aws_sdk_medialive.types.scte35_archive_allowed_flag.deserialize_json(
                data["archiveAllowedFlag"]
            )
        )
    if "deviceRestrictions" in data:
        import aws_sdk_medialive.types.scte35_device_restrictions

        out["device_restrictions"] = (
            aws_sdk_medialive.types.scte35_device_restrictions.deserialize_json(
                data["deviceRestrictions"]
            )
        )
    if "noRegionalBlackoutFlag" in data:
        import aws_sdk_medialive.types.scte35_no_regional_blackout_flag

        out["no_regional_blackout_flag"] = (
            aws_sdk_medialive.types.scte35_no_regional_blackout_flag.deserialize_json(
                data["noRegionalBlackoutFlag"]
            )
        )
    if "webDeliveryAllowedFlag" in data:
        import aws_sdk_medialive.types.scte35_web_delivery_allowed_flag

        out["web_delivery_allowed_flag"] = (
            aws_sdk_medialive.types.scte35_web_delivery_allowed_flag.deserialize_json(
                data["webDeliveryAllowedFlag"]
            )
        )
    return out
