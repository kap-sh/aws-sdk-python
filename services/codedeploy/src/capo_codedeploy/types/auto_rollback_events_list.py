"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoRollbackEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_rollback_event

AutoRollbackEventsList: TypeAlias = list[
    "capo_codedeploy.types.auto_rollback_event.AutoRollbackEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRollbackEventsList) -> list:
    import capo_codedeploy.types.auto_rollback_event

    out: list = []
    for item in value:
        out.append(
            capo_codedeploy.types.auto_rollback_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoRollbackEventsList:
    import capo_codedeploy.types.auto_rollback_event

    out: AutoRollbackEventsList = []
    for item in data:
        out.append(
            capo_codedeploy.types.auto_rollback_event.deserialize_aws_json_1_1(item)
        )
    return out
