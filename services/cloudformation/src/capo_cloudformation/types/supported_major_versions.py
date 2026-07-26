"""Generated from Smithy shape ``com.amazonaws.cloudformation#SupportedMajorVersions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.supported_major_version

SupportedMajorVersions: TypeAlias = list[
    "capo_cloudformation.types.supported_major_version.SupportedMajorVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedMajorVersions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> SupportedMajorVersions:
    out: SupportedMajorVersions = []
    for child in el.findall("member"):
        out.append(int(child.text or ""))
    return out


def serialize_query_flat(
    value: SupportedMajorVersions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SupportedMajorVersions:
    out: SupportedMajorVersions = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
