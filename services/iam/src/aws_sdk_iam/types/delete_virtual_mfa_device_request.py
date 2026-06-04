"""Generated from Smithy shape ``com.amazonaws.iam#DeleteVirtualMFADeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.serial_number_type


class DeleteVirtualMFADeviceRequest(TypedDict):
    serial_number: "aws_sdk_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteVirtualMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SerialNumber", str(value["serial_number"])))


def deserialize_query(el: Element) -> DeleteVirtualMFADeviceRequest:
    out: DeleteVirtualMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError(
            "DeleteVirtualMFADeviceRequest.serial_number required"
        )
    return out
