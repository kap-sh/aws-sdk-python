"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_metadata_filter

OpsMetadataFilterList: TypeAlias = list[
    "capo_ssm.types.ops_metadata_filter.OpsMetadataFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataFilterList) -> list:
    import capo_ssm.types.ops_metadata_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_metadata_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsMetadataFilterList:
    import capo_ssm.types.ops_metadata_filter

    out: OpsMetadataFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_metadata_filter.deserialize_aws_json_1_1(item))
    return out
