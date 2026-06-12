"""Generated from Smithy shape ``com.amazonaws.licensemanager#RegionStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.region_status
    import aws_sdk_license_manager.types.string

RegionStatusMap: TypeAlias = dict[
    "aws_sdk_license_manager.types.string.String",
    "aws_sdk_license_manager.types.region_status.RegionStatus",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RegionStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_license_manager.types.region_status

        out[key] = aws_sdk_license_manager.types.region_status.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionStatusMap:
    out: RegionStatusMap = {}
    for key, value in data.items():
        import aws_sdk_license_manager.types.region_status

        out[key] = aws_sdk_license_manager.types.region_status.deserialize_aws_json_1_1(
            value
        )
    return out
