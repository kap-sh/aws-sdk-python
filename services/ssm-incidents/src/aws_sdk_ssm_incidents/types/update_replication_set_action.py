"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateReplicationSetAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.add_region_action
    import aws_sdk_ssm_incidents.types.delete_region_action


class _UpdateReplicationSetAction_addRegionAction(TypedDict, closed=True):
    addRegionAction: "aws_sdk_ssm_incidents.types.add_region_action.AddRegionAction"


class _UpdateReplicationSetAction_deleteRegionAction(TypedDict, closed=True):
    deleteRegionAction: (
        "aws_sdk_ssm_incidents.types.delete_region_action.DeleteRegionAction"
    )


UpdateReplicationSetAction: TypeAlias = (
    _UpdateReplicationSetAction_addRegionAction
    | _UpdateReplicationSetAction_deleteRegionAction
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationSetAction) -> dict:
    if "addRegionAction" in value:
        import aws_sdk_ssm_incidents.types.add_region_action

        return {
            "addRegionAction": aws_sdk_ssm_incidents.types.add_region_action.serialize_json(
                value["addRegionAction"]
            )
        }
    elif "deleteRegionAction" in value:
        import aws_sdk_ssm_incidents.types.delete_region_action

        return {
            "deleteRegionAction": aws_sdk_ssm_incidents.types.delete_region_action.serialize_json(
                value["deleteRegionAction"]
            )
        }
    else:
        raise SerializationError("UpdateReplicationSetAction: no variant present")


def deserialize_json(data: dict) -> UpdateReplicationSetAction:
    if "addRegionAction" in data:
        import aws_sdk_ssm_incidents.types.add_region_action

        return {
            "addRegionAction": aws_sdk_ssm_incidents.types.add_region_action.deserialize_json(
                data["addRegionAction"]
            )
        }
    elif "deleteRegionAction" in data:
        import aws_sdk_ssm_incidents.types.delete_region_action

        return {
            "deleteRegionAction": aws_sdk_ssm_incidents.types.delete_region_action.deserialize_json(
                data["deleteRegionAction"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateReplicationSetAction: no recognized variant key"
        )
