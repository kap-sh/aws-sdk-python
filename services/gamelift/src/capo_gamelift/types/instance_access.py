"""Generated from Smithy shape ``com.amazonaws.gamelift#InstanceAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.instance_credentials
    import capo_gamelift.types.instance_id
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.operating_system


class InstanceAccess(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet containing the instance to be accessed.</p>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the instance to be accessed.</p>"""
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>IP address assigned to the instance.</p>"""
    operating_system: NotRequired[
        "capo_gamelift.types.operating_system.OperatingSystem"
    ]
    """<p>Operating system that is running on the instance.</p>"""
    credentials: NotRequired[
        "capo_gamelift.types.instance_credentials.InstanceCredentials"
    ]
    """<p>Security credentials that are required to access the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceAccess) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "operating_system" in value:
        import capo_gamelift.types.operating_system

        out["OperatingSystem"] = (
            capo_gamelift.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "credentials" in value:
        import capo_gamelift.types.instance_credentials

        out["Credentials"] = (
            capo_gamelift.types.instance_credentials.serialize_aws_json_1_1(
                value["credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAccess:
    out: InstanceAccess = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "OperatingSystem" in data:
        import capo_gamelift.types.operating_system

        out["operating_system"] = (
            capo_gamelift.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if "Credentials" in data:
        import capo_gamelift.types.instance_credentials

        out["credentials"] = (
            capo_gamelift.types.instance_credentials.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    return out
