"""Generated from Smithy shape ``com.amazonaws.emr#SetVisibleToAllUsersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.xml_string_list


class SetVisibleToAllUsersInput(TypedDict, closed=True):
    job_flow_ids: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>The unique identifier of the job flow (cluster).</p>"""
    visible_to_all_users: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>A value of <code>true</code> indicates that an IAM principal in the Amazon Web Services account can perform Amazon EMR actions on the cluster that the IAM policies attached to the principal allow. A value of <code>false</code> indicates that only the IAM principal that created the cluster and the Amazon Web Services root user can perform Amazon EMR actions on the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetVisibleToAllUsersInput) -> dict:
    out: dict = {}
    if "job_flow_ids" in value:
        import capo_emr.types.xml_string_list

        out["JobFlowIds"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["job_flow_ids"]
        )
    if "visible_to_all_users" in value:
        out["VisibleToAllUsers"] = value["visible_to_all_users"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetVisibleToAllUsersInput:
    out: SetVisibleToAllUsersInput = {}  # type: ignore[typeddict-item]
    if "JobFlowIds" in data:
        import capo_emr.types.xml_string_list

        out["job_flow_ids"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["JobFlowIds"]
        )
    if "VisibleToAllUsers" in data:
        out["visible_to_all_users"] = data["VisibleToAllUsers"]
    return out
