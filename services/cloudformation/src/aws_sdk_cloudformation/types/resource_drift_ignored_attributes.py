"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceDriftIgnoredAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_drift_ignored_attribute

ResourceDriftIgnoredAttributes: TypeAlias = list[
    "aws_sdk_cloudformation.types.resource_drift_ignored_attribute.ResourceDriftIgnoredAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceDriftIgnoredAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_drift_ignored_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_drift_ignored_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceDriftIgnoredAttributes:
    import aws_sdk_cloudformation.types.resource_drift_ignored_attribute

    out: ResourceDriftIgnoredAttributes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.resource_drift_ignored_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ResourceDriftIgnoredAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_drift_ignored_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_drift_ignored_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceDriftIgnoredAttributes:
    import aws_sdk_cloudformation.types.resource_drift_ignored_attribute

    out: ResourceDriftIgnoredAttributes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.resource_drift_ignored_attribute.deserialize_query(
                child
            )
        )
    return out
