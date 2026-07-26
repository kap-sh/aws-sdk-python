"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeConfigurationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node_configuration_option

ReservedNodeConfigurationOptionList: TypeAlias = list[
    "capo_redshift.types.reserved_node_configuration_option.ReservedNodeConfigurationOption"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeConfigurationOptionList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_redshift.types.reserved_node_configuration_option

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_configuration_option.serialize_query(
            item, pairs, f"{prefix}.ReservedNodeConfigurationOption.{n}"
        )


def deserialize_query(el: Element) -> ReservedNodeConfigurationOptionList:
    import capo_redshift.types.reserved_node_configuration_option

    out: ReservedNodeConfigurationOptionList = []
    for child in el.findall("ReservedNodeConfigurationOption"):
        out.append(
            capo_redshift.types.reserved_node_configuration_option.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ReservedNodeConfigurationOptionList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_redshift.types.reserved_node_configuration_option

    for n, item in enumerate(value, 1):
        capo_redshift.types.reserved_node_configuration_option.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ReservedNodeConfigurationOptionList:
    import capo_redshift.types.reserved_node_configuration_option

    out: ReservedNodeConfigurationOptionList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.reserved_node_configuration_option.deserialize_query(
                child
            )
        )
    return out
