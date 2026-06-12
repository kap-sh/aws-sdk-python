"""Generated from Smithy shape ``com.amazonaws.directconnect#Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.available_mac_sec_port_speeds
    import aws_sdk_direct_connect.types.available_port_speeds
    import aws_sdk_direct_connect.types.location_code
    import aws_sdk_direct_connect.types.location_name
    import aws_sdk_direct_connect.types.provider_list
    import aws_sdk_direct_connect.types.region


class Location(TypedDict):
    location_code: NotRequired[
        "aws_sdk_direct_connect.types.location_code.LocationCode"
    ]
    """<p>The code for the location.</p>"""
    location_name: NotRequired[
        "aws_sdk_direct_connect.types.location_name.LocationName"
    ]
    """<p>The name of the location. This includes the name of the colocation partner and the physical site of the building.</p>"""
    region: NotRequired["aws_sdk_direct_connect.types.region.Region"]
    """<p>The Amazon Web Services Region for the location.</p>"""
    available_port_speeds: NotRequired[
        "aws_sdk_direct_connect.types.available_port_speeds.AvailablePortSpeeds"
    ]
    """<p>The available port speeds for the location.</p>"""
    available_providers: NotRequired[
        "aws_sdk_direct_connect.types.provider_list.ProviderList"
    ]
    """<p>The name of the service provider for the location.</p>"""
    available_mac_sec_port_speeds: NotRequired[
        "aws_sdk_direct_connect.types.available_mac_sec_port_speeds.AvailableMacSecPortSpeeds"
    ]
    """<p>The available MAC Security (MACsec) port speeds for the location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    if "location_code" in value:
        out["locationCode"] = value["location_code"]
    if "location_name" in value:
        out["locationName"] = value["location_name"]
    if "region" in value:
        out["region"] = value["region"]
    if "available_port_speeds" in value:
        import aws_sdk_direct_connect.types.available_port_speeds

        out["availablePortSpeeds"] = (
            aws_sdk_direct_connect.types.available_port_speeds.serialize_aws_json_1_1(
                value["available_port_speeds"]
            )
        )
    if "available_providers" in value:
        import aws_sdk_direct_connect.types.provider_list

        out["availableProviders"] = (
            aws_sdk_direct_connect.types.provider_list.serialize_aws_json_1_1(
                value["available_providers"]
            )
        )
    if "available_mac_sec_port_speeds" in value:
        import aws_sdk_direct_connect.types.available_mac_sec_port_speeds

        out["availableMacSecPortSpeeds"] = (
            aws_sdk_direct_connect.types.available_mac_sec_port_speeds.serialize_aws_json_1_1(
                value["available_mac_sec_port_speeds"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "locationCode" in data:
        out["location_code"] = data["locationCode"]
    if "locationName" in data:
        out["location_name"] = data["locationName"]
    if "region" in data:
        out["region"] = data["region"]
    if "availablePortSpeeds" in data:
        import aws_sdk_direct_connect.types.available_port_speeds

        out["available_port_speeds"] = (
            aws_sdk_direct_connect.types.available_port_speeds.deserialize_aws_json_1_1(
                data["availablePortSpeeds"]
            )
        )
    if "availableProviders" in data:
        import aws_sdk_direct_connect.types.provider_list

        out["available_providers"] = (
            aws_sdk_direct_connect.types.provider_list.deserialize_aws_json_1_1(
                data["availableProviders"]
            )
        )
    if "availableMacSecPortSpeeds" in data:
        import aws_sdk_direct_connect.types.available_mac_sec_port_speeds

        out["available_mac_sec_port_speeds"] = (
            aws_sdk_direct_connect.types.available_mac_sec_port_speeds.deserialize_aws_json_1_1(
                data["availableMacSecPortSpeeds"]
            )
        )
    return out
