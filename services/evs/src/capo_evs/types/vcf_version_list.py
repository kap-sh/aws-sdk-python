"""Generated from Smithy shape ``com.amazonaws.evs#VcfVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.vcf_version_info

VcfVersionList: TypeAlias = list["capo_evs.types.vcf_version_info.VcfVersionInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VcfVersionList) -> list:
    import capo_evs.types.vcf_version_info

    out: list = []
    for item in value:
        out.append(capo_evs.types.vcf_version_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VcfVersionList:
    import capo_evs.types.vcf_version_info

    out: VcfVersionList = []
    for item in data:
        out.append(capo_evs.types.vcf_version_info.deserialize_aws_json_1_0(item))
    return out
