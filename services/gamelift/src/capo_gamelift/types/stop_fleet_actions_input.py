"""Generated from Smithy shape ``com.amazonaws.gamelift#StopFleetActionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_action_list
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model


class StopFleetActionsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to stop actions on. You can use either the fleet ID or ARN value.</p>"""
    actions: NotRequired["capo_gamelift.types.fleet_action_list.FleetActionList"]
    """<p>List of actions to suspend on the fleet. </p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The fleet location to stop fleet actions for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopFleetActionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "actions" in value:
        import capo_gamelift.types.fleet_action_list

        out["Actions"] = capo_gamelift.types.fleet_action_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopFleetActionsInput:
    out: StopFleetActionsInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "Actions" in data:
        import capo_gamelift.types.fleet_action_list

        out["actions"] = capo_gamelift.types.fleet_action_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if "Location" in data:
        out["location"] = data["Location"]
    return out
