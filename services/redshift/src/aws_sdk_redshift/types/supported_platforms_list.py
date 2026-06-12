"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedPlatformsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.supported_platform

SupportedPlatformsList: TypeAlias = list[
    "aws_sdk_redshift.types.supported_platform.SupportedPlatform"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedPlatformsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.supported_platform

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.supported_platform.serialize_query(
            item, pairs, f"{prefix}.SupportedPlatform.{n}"
        )


def deserialize_query(el: Element) -> SupportedPlatformsList:
    import aws_sdk_redshift.types.supported_platform

    out: SupportedPlatformsList = []
    for child in el.findall("SupportedPlatform"):
        out.append(aws_sdk_redshift.types.supported_platform.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SupportedPlatformsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.supported_platform

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.supported_platform.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SupportedPlatformsList:
    import aws_sdk_redshift.types.supported_platform

    out: SupportedPlatformsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.supported_platform.deserialize_query(child))
    return out
