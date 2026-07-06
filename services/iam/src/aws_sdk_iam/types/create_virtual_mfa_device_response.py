"""Generated from Smithy shape ``com.amazonaws.iam#CreateVirtualMFADeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.virtual_mfa_device


class CreateVirtualMFADeviceResponse(TypedDict, closed=True):
    virtual_mfa_device: "aws_sdk_iam.types.virtual_mfa_device.VirtualMFADevice"
    """<p>A structure containing details about the new virtual MFA device.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateVirtualMFADeviceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.virtual_mfa_device

    aws_sdk_iam.types.virtual_mfa_device.serialize_query(
        value["virtual_mfa_device"], pairs, f"{prefix}.VirtualMFADevice"
    )


def deserialize_query(el: Element) -> CreateVirtualMFADeviceResponse:
    out: CreateVirtualMFADeviceResponse = {}  # type: ignore[typeddict-item]
    child_virtual_mfa_device = el.find("VirtualMFADevice")
    if child_virtual_mfa_device is not None:
        import aws_sdk_iam.types.virtual_mfa_device

        out["virtual_mfa_device"] = (
            aws_sdk_iam.types.virtual_mfa_device.deserialize_query(
                child_virtual_mfa_device
            )
        )
    else:
        raise DeserializationError(
            "CreateVirtualMFADeviceResponse.virtual_mfa_device required"
        )
    return out
