"""Generated from Smithy shape ``com.amazonaws.dax#ParameterGroupStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.node_identifier_list
    import capo_dax.types.string


class ParameterGroupStatus(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the parameter group.</p>"""
    parameter_apply_status: NotRequired["capo_dax.types.string.String"]
    """<p>The status of parameter updates. </p>"""
    node_ids_to_reboot: NotRequired[
        "capo_dax.types.node_identifier_list.NodeIdentifierList"
    ]
    """<p>The node IDs of one or more nodes to be rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterGroupStatus) -> dict:
    out: dict = {}
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "parameter_apply_status" in value:
        out["ParameterApplyStatus"] = value["parameter_apply_status"]
    if "node_ids_to_reboot" in value:
        import capo_dax.types.node_identifier_list

        out["NodeIdsToReboot"] = (
            capo_dax.types.node_identifier_list.serialize_aws_json_1_1(
                value["node_ids_to_reboot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterGroupStatus:
    out: ParameterGroupStatus = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if "ParameterApplyStatus" in data:
        out["parameter_apply_status"] = data["ParameterApplyStatus"]
    if "NodeIdsToReboot" in data:
        import capo_dax.types.node_identifier_list

        out["node_ids_to_reboot"] = (
            capo_dax.types.node_identifier_list.deserialize_aws_json_1_1(
                data["NodeIdsToReboot"]
            )
        )
    return out
