"""Generated from Smithy shape ``com.amazonaws.iam#GetMFADeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.serial_number_type
    import aws_sdk_iam.types.user_name_type


class GetMFADeviceRequest(TypedDict):
    serial_number: "aws_sdk_iam.types.serial_number_type.serialNumberType"
    """<p>Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">ARNs</a>.</p>"""
    user_name: NotRequired["aws_sdk_iam.types.user_name_type.userNameType"]
    """<p>The friendly name identifying the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.SerialNumber", str(value["serial_number"])))
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> GetMFADeviceRequest:
    out: GetMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("GetMFADeviceRequest.serial_number required")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    return out
