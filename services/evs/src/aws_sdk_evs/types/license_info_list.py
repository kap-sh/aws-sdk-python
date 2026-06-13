"""Generated from Smithy shape ``com.amazonaws.evs#LicenseInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.license_info

LicenseInfoList: TypeAlias = list["aws_sdk_evs.types.license_info.LicenseInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseInfoList) -> list:
    import aws_sdk_evs.types.license_info

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.license_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseInfoList:
    import aws_sdk_evs.types.license_info

    out: LicenseInfoList = []
    for item in data:
        out.append(aws_sdk_evs.types.license_info.deserialize_aws_json_1_0(item))
    return out
