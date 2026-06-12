"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.aws_location
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.location
    import aws_sdk_networkmanager.types.site_id


class UpdateDeviceRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "aws_sdk_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    aws_location: NotRequired["aws_sdk_networkmanager.types.aws_location.AWSLocation"]
    """<p>The Amazon Web Services location of the device, if applicable. For an on-premises device, you can omit this parameter.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the device.</p> <p>Constraints: Maximum length of 256 characters.</p>"""
    type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of the device.</p>"""
    vendor: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The vendor of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    model: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The model of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    serial_number: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The serial number of the device.</p> <p>Constraints: Maximum length of 128 characters.</p>"""
    location: NotRequired["aws_sdk_networkmanager.types.location.Location"]
    site_id: NotRequired["aws_sdk_networkmanager.types.site_id.SiteId"]
    """<p>The ID of the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceRequest) -> dict:
    out: dict = {}
    if "aws_location" in value:
        import aws_sdk_networkmanager.types.aws_location

        out["AWSLocation"] = aws_sdk_networkmanager.types.aws_location.serialize_json(
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
        import aws_sdk_networkmanager.types.location

        out["Location"] = aws_sdk_networkmanager.types.location.serialize_json(
            value["location"]
        )
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    return out


def deserialize_json(data: dict) -> UpdateDeviceRequest:
    out: UpdateDeviceRequest = {}  # type: ignore[typeddict-item]
    if "AWSLocation" in data:
        import aws_sdk_networkmanager.types.aws_location

        out["aws_location"] = (
            aws_sdk_networkmanager.types.aws_location.deserialize_json(
                data["AWSLocation"]
            )
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
        import aws_sdk_networkmanager.types.location

        out["location"] = aws_sdk_networkmanager.types.location.deserialize_json(
            data["Location"]
        )
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    return out
