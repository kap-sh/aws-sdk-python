"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSetAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_attribute

ConfigurationSetAttributeList: TypeAlias = list[
    "aws_sdk_ses.types.configuration_set_attribute.ConfigurationSetAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSetAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.configuration_set_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.configuration_set_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ConfigurationSetAttributeList:
    import aws_sdk_ses.types.configuration_set_attribute

    out: ConfigurationSetAttributeList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_ses.types.configuration_set_attribute.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ConfigurationSetAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.configuration_set_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.configuration_set_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ConfigurationSetAttributeList:
    import aws_sdk_ses.types.configuration_set_attribute

    out: ConfigurationSetAttributeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ses.types.configuration_set_attribute.deserialize_query(child)
        )
    return out
