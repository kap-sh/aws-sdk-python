"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.node_configuration_options_filter

NodeConfigurationOptionsFilterList: TypeAlias = list[
    "aws_sdk_redshift.types.node_configuration_options_filter.NodeConfigurationOptionsFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeConfigurationOptionsFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.node_configuration_options_filter

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.node_configuration_options_filter.serialize_query(
            item, pairs, f"{prefix}.NodeConfigurationOptionsFilter.{n}"
        )


def deserialize_query(el: Element) -> NodeConfigurationOptionsFilterList:
    import aws_sdk_redshift.types.node_configuration_options_filter

    out: NodeConfigurationOptionsFilterList = []
    for child in el.findall("NodeConfigurationOptionsFilter"):
        out.append(
            aws_sdk_redshift.types.node_configuration_options_filter.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: NodeConfigurationOptionsFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.node_configuration_options_filter

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.node_configuration_options_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> NodeConfigurationOptionsFilterList:
    import aws_sdk_redshift.types.node_configuration_options_filter

    out: NodeConfigurationOptionsFilterList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.node_configuration_options_filter.deserialize_query(
                child
            )
        )
    return out
