"""Generated from Smithy shape ``com.amazonaws.iam#virtualMFADeviceListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.virtual_mfa_device

virtualMFADeviceListType: TypeAlias = list[
    "aws_sdk_iam.types.virtual_mfa_device.VirtualMFADevice"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: virtualMFADeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.virtual_mfa_device

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.virtual_mfa_device.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> virtualMFADeviceListType:
    import aws_sdk_iam.types.virtual_mfa_device

    out: virtualMFADeviceListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.virtual_mfa_device.deserialize_query(child))
    return out


def serialize_query_flat(
    value: virtualMFADeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.virtual_mfa_device

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.virtual_mfa_device.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> virtualMFADeviceListType:
    import aws_sdk_iam.types.virtual_mfa_device

    out: virtualMFADeviceListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.virtual_mfa_device.deserialize_query(child))
    return out
