"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarksSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.nielsen_cbet
    import aws_sdk_medialive.types.nielsen_naes_ii_nw
    import aws_sdk_medialive.types.nielsen_watermarks_distribution_types


class NielsenWatermarksSettings(TypedDict):
    nielsen_cbet_settings: NotRequired[
        "aws_sdk_medialive.types.nielsen_cbet.NielsenCBET"
    ]
    """Complete these fields only if you want to insert watermarks of type Nielsen CBET"""
    nielsen_distribution_type: NotRequired[
        "aws_sdk_medialive.types.nielsen_watermarks_distribution_types.NielsenWatermarksDistributionTypes"
    ]
    """Choose the distribution types that you want to assign to the watermarks: - PROGRAM_CONTENT - FINAL_DISTRIBUTOR"""
    nielsen_naes_ii_nw_settings: NotRequired[
        "aws_sdk_medialive.types.nielsen_naes_ii_nw.NielsenNaesIiNw"
    ]
    """Complete these fields only if you want to insert watermarks of type Nielsen NAES II (N2) and Nielsen NAES VI (NW)."""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenWatermarksSettings) -> dict:
    out: dict = {}
    if "nielsen_cbet_settings" in value:
        import aws_sdk_medialive.types.nielsen_cbet

        out["nielsenCbetSettings"] = (
            aws_sdk_medialive.types.nielsen_cbet.serialize_json(
                value["nielsen_cbet_settings"]
            )
        )
    if "nielsen_distribution_type" in value:
        import aws_sdk_medialive.types.nielsen_watermarks_distribution_types

        out["nielsenDistributionType"] = (
            aws_sdk_medialive.types.nielsen_watermarks_distribution_types.serialize_json(
                value["nielsen_distribution_type"]
            )
        )
    if "nielsen_naes_ii_nw_settings" in value:
        import aws_sdk_medialive.types.nielsen_naes_ii_nw

        out["nielsenNaesIiNwSettings"] = (
            aws_sdk_medialive.types.nielsen_naes_ii_nw.serialize_json(
                value["nielsen_naes_ii_nw_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> NielsenWatermarksSettings:
    out: NielsenWatermarksSettings = {}  # type: ignore[typeddict-item]
    if "nielsenCbetSettings" in data:
        import aws_sdk_medialive.types.nielsen_cbet

        out["nielsen_cbet_settings"] = (
            aws_sdk_medialive.types.nielsen_cbet.deserialize_json(
                data["nielsenCbetSettings"]
            )
        )
    if "nielsenDistributionType" in data:
        import aws_sdk_medialive.types.nielsen_watermarks_distribution_types

        out["nielsen_distribution_type"] = (
            aws_sdk_medialive.types.nielsen_watermarks_distribution_types.deserialize_json(
                data["nielsenDistributionType"]
            )
        )
    if "nielsenNaesIiNwSettings" in data:
        import aws_sdk_medialive.types.nielsen_naes_ii_nw

        out["nielsen_naes_ii_nw_settings"] = (
            aws_sdk_medialive.types.nielsen_naes_ii_nw.deserialize_json(
                data["nielsenNaesIiNwSettings"]
            )
        )
    return out
