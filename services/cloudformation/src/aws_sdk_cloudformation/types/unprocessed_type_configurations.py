"""Generated from Smithy shape ``com.amazonaws.cloudformation#UnprocessedTypeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.type_configuration_identifier

UnprocessedTypeConfigurations: TypeAlias = list[
    "aws_sdk_cloudformation.types.type_configuration_identifier.TypeConfigurationIdentifier"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: UnprocessedTypeConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_configuration_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_configuration_identifier.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> UnprocessedTypeConfigurations:
    import aws_sdk_cloudformation.types.type_configuration_identifier

    out: UnprocessedTypeConfigurations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.type_configuration_identifier.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: UnprocessedTypeConfigurations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_configuration_identifier

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_configuration_identifier.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> UnprocessedTypeConfigurations:
    import aws_sdk_cloudformation.types.type_configuration_identifier

    out: UnprocessedTypeConfigurations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.type_configuration_identifier.deserialize_query(
                child
            )
        )
    return out
