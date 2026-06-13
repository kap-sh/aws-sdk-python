"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#TargetAction``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters


class _TargetAction_createSnapshot(TypedDict):
    createSnapshot: "aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters.CreateSnapshotScheduleActionParameters"


TargetAction: TypeAlias = _TargetAction_createSnapshot


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetAction) -> dict:
    if "createSnapshot" in value:
        import aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters

        return {
            "createSnapshot": aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters.serialize_aws_json_1_1(
                value["createSnapshot"]
            )
        }
    else:
        raise SerializationError("TargetAction: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TargetAction:
    if "createSnapshot" in data:
        import aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters

        return {
            "createSnapshot": aws_sdk_redshift_serverless.types.create_snapshot_schedule_action_parameters.deserialize_aws_json_1_1(
                data["createSnapshot"]
            )
        }
    else:
        raise DeserializationError("TargetAction: no recognized variant key")
