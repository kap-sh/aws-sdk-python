"""Generated from Smithy shape ``com.amazonaws.redshift#GetReservedNodeExchangeConfigurationOptionsOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.reserved_node_configuration_option_list
    import aws_sdk_redshift.types.string


class GetReservedNodeExchangeConfigurationOptionsOutputMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A pagination token provided by a previous <code>GetReservedNodeExchangeConfigurationOptions</code> request.</p>"""
    reserved_node_configuration_option_list: NotRequired[
        "aws_sdk_redshift.types.reserved_node_configuration_option_list.ReservedNodeConfigurationOptionList"
    ]
    """<p>the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node. Details include the node type, the price, the node count, and the offering type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetReservedNodeExchangeConfigurationOptionsOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_node_configuration_option_list" in value:
        import aws_sdk_redshift.types.reserved_node_configuration_option_list

        aws_sdk_redshift.types.reserved_node_configuration_option_list.serialize_query(
            value["reserved_node_configuration_option_list"],
            pairs,
            f"{prefix}.ReservedNodeConfigurationOptionList",
        )


def deserialize_query(
    el: Element,
) -> GetReservedNodeExchangeConfigurationOptionsOutputMessage:
    out: GetReservedNodeExchangeConfigurationOptionsOutputMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_node_configuration_option_list = el.find(
        "ReservedNodeConfigurationOptionList"
    )
    if child_reserved_node_configuration_option_list is not None:
        import aws_sdk_redshift.types.reserved_node_configuration_option_list

        out["reserved_node_configuration_option_list"] = (
            aws_sdk_redshift.types.reserved_node_configuration_option_list.deserialize_query(
                child_reserved_node_configuration_option_list
            )
        )
    return out
