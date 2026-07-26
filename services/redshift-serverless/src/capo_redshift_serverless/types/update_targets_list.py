"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateTargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.update_target

UpdateTargetsList: TypeAlias = list[
    "capo_redshift_serverless.types.update_target.UpdateTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTargetsList) -> list:
    import capo_redshift_serverless.types.update_target

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.update_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateTargetsList:
    import capo_redshift_serverless.types.update_target

    out: UpdateTargetsList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.update_target.deserialize_aws_json_1_1(item)
        )
    return out
