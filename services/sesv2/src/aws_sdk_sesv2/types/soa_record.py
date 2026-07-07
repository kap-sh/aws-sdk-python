"""Generated from Smithy shape ``com.amazonaws.sesv2#SOARecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.admin_email
    import aws_sdk_sesv2.types.primary_name_server
    import aws_sdk_sesv2.types.serial_number


class SOARecord(TypedDict, closed=True):
    primary_name_server: NotRequired[
        "aws_sdk_sesv2.types.primary_name_server.PrimaryNameServer"
    ]
    """<p>Primary name server specified in the SOA record.</p>"""
    admin_email: NotRequired["aws_sdk_sesv2.types.admin_email.AdminEmail"]
    """<p>Administrative contact email from the SOA record.</p>"""
    serial_number: "aws_sdk_sesv2.types.serial_number.SerialNumber"
    """<p>Serial number from the SOA record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SOARecord) -> dict:
    out: dict = {}
    if "primary_name_server" in value:
        out["PrimaryNameServer"] = value["primary_name_server"]
    if "admin_email" in value:
        out["AdminEmail"] = value["admin_email"]
    out["SerialNumber"] = value.get("serial_number", 0)
    return out


def deserialize_json(data: dict) -> SOARecord:
    out: SOARecord = {}  # type: ignore[typeddict-item]
    if "PrimaryNameServer" in data:
        out["primary_name_server"] = data["PrimaryNameServer"]
    if "AdminEmail" in data:
        out["admin_email"] = data["AdminEmail"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    else:
        out["serial_number"] = 0
    return out
