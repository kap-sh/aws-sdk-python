"""Generated from Smithy shape ``com.amazonaws.odb#SystemVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.system_version_summary

SystemVersionList: TypeAlias = list[
    "capo_odb.types.system_version_summary.SystemVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SystemVersionList) -> list:
    import capo_odb.types.system_version_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.system_version_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SystemVersionList:
    import capo_odb.types.system_version_summary

    out: SystemVersionList = []
    for item in data:
        out.append(capo_odb.types.system_version_summary.deserialize_aws_json_1_0(item))
    return out
