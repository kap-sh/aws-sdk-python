"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#AssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.association

AssociationList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.association.Association"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationList) -> list:
    import aws_sdk_redshift_serverless.types.association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_serverless.types.association.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationList:
    import aws_sdk_redshift_serverless.types.association

    out: AssociationList = []
    for item in data:
        out.append(
            aws_sdk_redshift_serverless.types.association.deserialize_aws_json_1_1(item)
        )
    return out
