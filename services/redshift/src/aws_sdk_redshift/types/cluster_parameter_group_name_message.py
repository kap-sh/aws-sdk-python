"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterParameterGroupNameMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ClusterParameterGroupNameMessage(TypedDict, closed=True):
    parameter_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group.</p>"""
    parameter_group_status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterParameterGroupNameMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "parameter_group_status" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupStatus", str(value["parameter_group_status"]))
        )


def deserialize_query(el: Element) -> ClusterParameterGroupNameMessage:
    out: ClusterParameterGroupNameMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_parameter_group_status = el.find("ParameterGroupStatus")
    if child_parameter_group_status is not None:
        out["parameter_group_status"] = str(child_parameter_group_status.text or "")
    return out
