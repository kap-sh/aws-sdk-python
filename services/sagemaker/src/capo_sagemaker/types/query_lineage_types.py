"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryLineageTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.lineage_type

QueryLineageTypes: TypeAlias = list["capo_sagemaker.types.lineage_type.LineageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryLineageTypes) -> list:
    import capo_sagemaker.types.lineage_type

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.lineage_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryLineageTypes:
    import capo_sagemaker.types.lineage_type

    out: QueryLineageTypes = []
    for item in data:
        out.append(capo_sagemaker.types.lineage_type.deserialize_aws_json_1_1(item))
    return out
