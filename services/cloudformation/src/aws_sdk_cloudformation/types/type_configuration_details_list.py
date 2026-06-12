"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeConfigurationDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.type_configuration_details

TypeConfigurationDetailsList: TypeAlias = list[
    "aws_sdk_cloudformation.types.type_configuration_details.TypeConfigurationDetails"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeConfigurationDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_configuration_details

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_configuration_details.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TypeConfigurationDetailsList:
    import aws_sdk_cloudformation.types.type_configuration_details

    out: TypeConfigurationDetailsList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.type_configuration_details.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TypeConfigurationDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.type_configuration_details

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.type_configuration_details.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TypeConfigurationDetailsList:
    import aws_sdk_cloudformation.types.type_configuration_details

    out: TypeConfigurationDetailsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.type_configuration_details.deserialize_query(
                child
            )
        )
    return out
