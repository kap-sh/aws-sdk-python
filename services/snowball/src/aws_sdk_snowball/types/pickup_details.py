"""Generated from Smithy shape ``com.amazonaws.snowball#PickupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.device_pickup_id
    import aws_sdk_snowball.types.email
    import aws_sdk_snowball.types.phone_number
    import aws_sdk_snowball.types.string
    import aws_sdk_snowball.types.timestamp


class PickupDetails(TypedDict, closed=True):
    name: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The name of the person picking up the device.</p>"""
    phone_number: NotRequired["aws_sdk_snowball.types.phone_number.PhoneNumber"]
    """<p>The phone number of the person picking up the device.</p>"""
    email: NotRequired["aws_sdk_snowball.types.email.Email"]
    """<p>The email address of the person picking up the device.</p>"""
    identification_number: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The number on the credential identifying the person picking up the device.</p>"""
    identification_expiration_date: NotRequired[
        "aws_sdk_snowball.types.timestamp.Timestamp"
    ]
    """<p>Expiration date of the credential identifying the person picking up the device.</p>"""
    identification_issuing_org: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Organization that issued the credential identifying the person picking up the device.</p>"""
    device_pickup_id: NotRequired[
        "aws_sdk_snowball.types.device_pickup_id.DevicePickupId"
    ]
    """<p>The unique ID for a device that will be picked up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PickupDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "email" in value:
        out["Email"] = value["email"]
    if "identification_number" in value:
        out["IdentificationNumber"] = value["identification_number"]
    if "identification_expiration_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["IdentificationExpirationDate"] = (
            aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
                value["identification_expiration_date"]
            )
        )
    if "identification_issuing_org" in value:
        out["IdentificationIssuingOrg"] = value["identification_issuing_org"]
    if "device_pickup_id" in value:
        out["DevicePickupId"] = value["device_pickup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PickupDetails:
    out: PickupDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "Email" in data:
        out["email"] = data["Email"]
    if "IdentificationNumber" in data:
        out["identification_number"] = data["IdentificationNumber"]
    if "IdentificationExpirationDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["identification_expiration_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["IdentificationExpirationDate"]
            )
        )
    if "IdentificationIssuingOrg" in data:
        out["identification_issuing_org"] = data["IdentificationIssuingOrg"]
    if "DevicePickupId" in data:
        out["device_pickup_id"] = data["DevicePickupId"]
    return out
