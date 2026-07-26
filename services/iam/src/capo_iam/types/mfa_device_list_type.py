"""Generated from Smithy shape ``com.amazonaws.iam#mfaDeviceListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.mfa_device

mfaDeviceListType: TypeAlias = list["capo_iam.types.mfa_device.MFADevice"]


# --- awsQuery ser/de ---
def serialize_query(
    value: mfaDeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.mfa_device

    for n, item in enumerate(value, 1):
        capo_iam.types.mfa_device.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> mfaDeviceListType:
    import capo_iam.types.mfa_device

    out: mfaDeviceListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.mfa_device.deserialize_query(child))
    return out


def serialize_query_flat(
    value: mfaDeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.mfa_device

    for n, item in enumerate(value, 1):
        capo_iam.types.mfa_device.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> mfaDeviceListType:
    import capo_iam.types.mfa_device

    out: mfaDeviceListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.mfa_device.deserialize_query(child))
    return out
