"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationSyncCompliance``."""

from typing import Literal, TypeAlias, cast

AssociationSyncCompliance: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationSyncCompliance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationSyncCompliance:
    return cast(AssociationSyncCompliance, data)
