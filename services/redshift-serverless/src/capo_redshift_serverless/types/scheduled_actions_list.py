"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ScheduledActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.scheduled_action_association

ScheduledActionsList: TypeAlias = list[
    "capo_redshift_serverless.types.scheduled_action_association.ScheduledActionAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledActionsList) -> list:
    import capo_redshift_serverless.types.scheduled_action_association

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.scheduled_action_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledActionsList:
    import capo_redshift_serverless.types.scheduled_action_association

    out: ScheduledActionsList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.scheduled_action_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
