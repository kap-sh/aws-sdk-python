"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScannedResourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.scanned_resource_identifier

ScannedResourceIdentifiers: TypeAlias = list[
    "aws_sdk_cloudformation.types.scanned_resource_identifier.ScannedResourceIdentifier"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScannedResourceIdentifiers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.scanned_resource_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.scanned_resource_identifier.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ScannedResourceIdentifiers:
    import aws_sdk_cloudformation.types.scanned_resource_identifier

    out: ScannedResourceIdentifiers = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.scanned_resource_identifier.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ScannedResourceIdentifiers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.scanned_resource_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.scanned_resource_identifier.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ScannedResourceIdentifiers:
    import aws_sdk_cloudformation.types.scanned_resource_identifier

    out: ScannedResourceIdentifiers = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.scanned_resource_identifier.deserialize_query(
                child
            )
        )
    return out
