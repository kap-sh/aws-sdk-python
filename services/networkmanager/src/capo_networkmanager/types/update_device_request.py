"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_location
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.location
    import capo_networkmanager.types.site_id


class UpdateDeviceRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    aws_location: NotRequired["capo_networkmanager.types.aws_location.AWSLocation"]
    """<p>The Amazon Web Services location of the device, if applicable. For an on-premises device, you can omit this parameter.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the device.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    type: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The type of the device.</p>"""
    vendor: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The vendor of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    model: NotRequired["capo_networkmanager.types.constrained_string.ConstrainedString"]
    """<p>The model of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    serial_number: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The serial number of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    location: NotRequired["capo_networkmanager.types.location.Location"]
    site_id: NotRequired["capo_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateDeviceRequest:
    out: UpdateDeviceRequest = {}  # type: ignore[typeddict-item]
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
    return out
