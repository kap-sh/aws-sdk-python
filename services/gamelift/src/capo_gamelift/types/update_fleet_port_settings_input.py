"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateFleetPortSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.ip_permissions_list


class UpdateFleetPortSettingsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to update port settings for. You can use either the fleet ID or ARN value.</p>"""
    inbound_permission_authorizations: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>A collection of port settings to be added to the fleet resource.</p>"""
    inbound_permission_revocations: NotRequired[
        "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
    ]
    """<p>A collection of port settings to be removed from the fleet resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetPortSettingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "inbound_permission_authorizations" in value:
        import capo_gamelift.types.ip_permissions_list

        out["InboundPermissionAuthorizations"] = (
            capo_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["inbound_permission_authorizations"]
            )
        )
    if "inbound_permission_revocations" in value:
        import capo_gamelift.types.ip_permissions_list

        out["InboundPermissionRevocations"] = (
            capo_gamelift.types.ip_permissions_list.serialize_aws_json_1_1(
                value["inbound_permission_revocations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetPortSettingsInput:
    out: UpdateFleetPortSettingsInput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "InboundPermissionAuthorizations" in data:
        import capo_gamelift.types.ip_permissions_list

        out["inbound_permission_authorizations"] = (
            capo_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InboundPermissionAuthorizations"]
            )
        )
    if "InboundPermissionRevocations" in data:
        import capo_gamelift.types.ip_permissions_list

        out["inbound_permission_revocations"] = (
            capo_gamelift.types.ip_permissions_list.deserialize_aws_json_1_1(
                data["InboundPermissionRevocations"]
            )
        )
    return out
