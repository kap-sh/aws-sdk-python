"""Generated from Smithy shape ``com.amazonaws.evs#InstanceTypeEsxVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.instance_type_esx_versions_info

InstanceTypeEsxVersionsList: TypeAlias = list[
    "aws_sdk_evs.types.instance_type_esx_versions_info.InstanceTypeEsxVersionsInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeEsxVersionsList) -> list:
    import aws_sdk_evs.types.instance_type_esx_versions_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_evs.types.instance_type_esx_versions_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceTypeEsxVersionsList:
    import aws_sdk_evs.types.instance_type_esx_versions_info

    out: InstanceTypeEsxVersionsList = []
    for item in data:
        out.append(
            aws_sdk_evs.types.instance_type_esx_versions_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
