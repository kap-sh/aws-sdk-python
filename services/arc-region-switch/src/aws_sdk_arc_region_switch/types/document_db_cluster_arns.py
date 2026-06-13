"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DocumentDbClusterArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.document_db_cluster_arn

DocumentDbClusterArns: TypeAlias = list[
    "aws_sdk_arc_region_switch.types.document_db_cluster_arn.DocumentDbClusterArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentDbClusterArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DocumentDbClusterArns:
    return list(data)
