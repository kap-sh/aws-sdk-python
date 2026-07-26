"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RecoveryPointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.recovery_point

RecoveryPointList: TypeAlias = list[
    "capo_redshift_serverless.types.recovery_point.RecoveryPoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryPointList) -> list:
    import capo_redshift_serverless.types.recovery_point

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.recovery_point.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecoveryPointList:
    import capo_redshift_serverless.types.recovery_point

    out: RecoveryPointList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.recovery_point.deserialize_aws_json_1_1(item)
        )
    return out
