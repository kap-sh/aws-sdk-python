"""Generated from Smithy shape ``com.amazonaws.iam#MFADevice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.serial_number_type
    import aws_sdk_iam.types.user_name_type


class MFADevice(TypedDict, closed=True):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The user with whom the MFA device is associated.</p>"""
    serial_number: "aws_sdk_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.</p>"""
    enable_date: "aws_sdk_iam.types.date_type.dateType"
    """<p>The date when the MFA device was enabled for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MFADevice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.SerialNumber", str(value["serial_number"])))
    import aws_sdk_iam.types.date_type

    aws_sdk_iam.types.date_type.serialize_query(
        value["enable_date"], pairs, f"{prefix}.EnableDate"
    )


def deserialize_query(el: Element) -> MFADevice:
    out: MFADevice = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("MFADevice.user_name required")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("MFADevice.serial_number required")
    child_enable_date = el.find("EnableDate")
    if child_enable_date is not None:
        import aws_sdk_iam.types.date_type

        out["enable_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_enable_date
        )
    else:
        raise DeserializationError("MFADevice.enable_date required")
    return out
