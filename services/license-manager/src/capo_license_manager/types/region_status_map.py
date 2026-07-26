"""Generated from Smithy shape ``com.amazonaws.licensemanager#RegionStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.region_status
    import capo_license_manager.types.string

RegionStatusMap: TypeAlias = dict[
    "capo_license_manager.types.string.String",
    "capo_license_manager.types.region_status.RegionStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RegionStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_license_manager.types.region_status

        out[key] = capo_license_manager.types.region_status.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionStatusMap:
    out: RegionStatusMap = {}
    for key, value in data.items():
        import capo_license_manager.types.region_status

        out[key] = capo_license_manager.types.region_status.deserialize_aws_json_1_1(
            value
        )
    return out
