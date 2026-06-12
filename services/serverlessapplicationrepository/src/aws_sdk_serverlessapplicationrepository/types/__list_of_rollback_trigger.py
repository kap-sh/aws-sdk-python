"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfRollbackTrigger``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.rollback_trigger

__listOfRollbackTrigger: TypeAlias = list[
    "aws_sdk_serverlessapplicationrepository.types.rollback_trigger.RollbackTrigger"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRollbackTrigger) -> list:
    import aws_sdk_serverlessapplicationrepository.types.rollback_trigger

    out: list = []
    for item in value:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.rollback_trigger.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfRollbackTrigger:
    import aws_sdk_serverlessapplicationrepository.types.rollback_trigger

    out: __listOfRollbackTrigger = []
    for item in data:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.rollback_trigger.deserialize_json(
                item
            )
        )
    return out
