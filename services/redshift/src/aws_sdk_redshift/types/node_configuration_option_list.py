"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.node_configuration_option

NodeConfigurationOptionList: TypeAlias = list[
    "aws_sdk_redshift.types.node_configuration_option.NodeConfigurationOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeConfigurationOptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.node_configuration_option

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.node_configuration_option.serialize_query(
            item, pairs, f"{prefix}.NodeConfigurationOption.{n}"
        )


def deserialize_query(el: Element) -> NodeConfigurationOptionList:
    import aws_sdk_redshift.types.node_configuration_option

    out: NodeConfigurationOptionList = []
    for child in el.findall("NodeConfigurationOption"):
        out.append(
            aws_sdk_redshift.types.node_configuration_option.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: NodeConfigurationOptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.node_configuration_option

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.node_configuration_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeConfigurationOptionList:
    import aws_sdk_redshift.types.node_configuration_option

    out: NodeConfigurationOptionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.node_configuration_option.deserialize_query(child)
        )
    return out
