"""Generated from Smithy shape ``com.amazonaws.odb#GiVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.gi_version_summary

GiVersionList: TypeAlias = list["capo_odb.types.gi_version_summary.GiVersionSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GiVersionList) -> list:
    import capo_odb.types.gi_version_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.gi_version_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> GiVersionList:
    import capo_odb.types.gi_version_summary

    out: GiVersionList = []
    for item in data:
        out.append(capo_odb.types.gi_version_summary.deserialize_aws_json_1_0(item))
    return out
