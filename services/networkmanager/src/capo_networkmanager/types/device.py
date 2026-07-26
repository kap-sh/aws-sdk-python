"""Generated from Smithy shape ``com.amazonaws.networkmanager#Device``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_location
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.device_arn
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.device_state
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.site_id
    import capo_networkmanager.types.tag_list


class Device(TypedDict, closed=True):
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    device_arn: NotRequired["capo_networkmanager.types.device_arn.DeviceArn"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    aws_location: NotRequired["capo_networkmanager.types.aws_location.AWSLocation"]
    """<p>The Amazon Web Services location of the device.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the device.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The device type.</p>"""
    vendor: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The device vendor.</p>"""
    model: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The device model.</p>"""
    serial_number: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The device serial number.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    """<p>The site location.</p>"""
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The site ID.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the site was created.</p>"""
    state: NotRequired["capo_networkmanager.types.device_state.DeviceState"]
    """<p>The device state.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "aws_location" in value:
        import capo_networkmanager.types.aws_location

        out["AWSLocation"] = capo_networkmanager.types.aws_location.serialize_json(
            value["aws_location"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "vendor" in value:
        out["Vendor"] = value["vendor"]
    if "model" in value:
        out["Model"] = value["model"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "location" in value:
        import capo_networkmanager.types.location

        out["Location"] = capo_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.device_state

        out["State"] = capo_networkmanager.types.device_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "DeviceArn" in data:
        out["device_arn"] = data["DeviceArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "AWSLocation" in data:
        import capo_networkmanager.types.aws_location

        out["aws_location"] = capo_networkmanager.types.aws_location.deserialize_json(
            data["AWSLocation"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Vendor" in data:
        out["vendor"] = data["Vendor"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "Location" in data:
        import capo_networkmanager.types.location

        out["location"] = capo_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import capo_networkmanager.types.device_state

        out["state"] = capo_networkmanager.types.device_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
