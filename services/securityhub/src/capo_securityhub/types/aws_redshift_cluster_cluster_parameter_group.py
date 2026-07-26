"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterParameterGroup(TypedDict, closed=True):
    cluster_parameter_status_list: NotRequired[
        "capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.AwsRedshiftClusterClusterParameterStatusList"
    ]
    """<p>The list of parameter statuses.</p>"""
    parameter_apply_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of updates to the parameters.</p>"""
    parameter_group_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the parameter group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterParameterGroup) -> dict:
    out: dict = {}
    if "cluster_parameter_status_list" in value:
        import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list

        out["ClusterParameterStatusList"] = (
            capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.serialize_json(
                value["cluster_parameter_status_list"]
            )
        )
    if "parameter_apply_status" in value:
        out["ParameterApplyStatus"] = value["parameter_apply_status"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterClusterParameterGroup:
    out: AwsRedshiftClusterClusterParameterGroup = {}  # type: ignore[typeddict-item]
    if "ClusterParameterStatusList" in data:
        import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list

        out["cluster_parameter_status_list"] = (
            capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.deserialize_json(
                data["ClusterParameterStatusList"]
            )
        )
    if "ParameterApplyStatus" in data:
        out["parameter_apply_status"] = data["ParameterApplyStatus"]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    return out
