"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.node_configuration_option_list
    import aws_sdk_redshift.types.string


class NodeConfigurationOptionsMessage(TypedDict):
    node_configuration_option_list: NotRequired[
        "aws_sdk_redshift.types.node_configuration_option_list.NodeConfigurationOptionList"
    ]
    """<p>A list of valid node configurations.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeConfigurationOptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "node_configuration_option_list" in value:
        import aws_sdk_redshift.types.node_configuration_option_list

        aws_sdk_redshift.types.node_configuration_option_list.serialize_query(
            value["node_configuration_option_list"],
            pairs,
            f"{prefix}.NodeConfigurationOptionList",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> NodeConfigurationOptionsMessage:
    out: NodeConfigurationOptionsMessage = {}  # type: ignore[typeddict-item]
    child_node_configuration_option_list = el.find("NodeConfigurationOptionList")
    if child_node_configuration_option_list is not None:
        import aws_sdk_redshift.types.node_configuration_option_list

        out["node_configuration_option_list"] = (
            aws_sdk_redshift.types.node_configuration_option_list.deserialize_query(
                child_node_configuration_option_list
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
