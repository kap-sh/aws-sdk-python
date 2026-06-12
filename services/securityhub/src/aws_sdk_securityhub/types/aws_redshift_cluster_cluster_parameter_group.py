"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterParameterGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsRedshiftClusterClusterParameterGroup(TypedDict):
    cluster_parameter_status_list: NotRequired[
        "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.AwsRedshiftClusterClusterParameterStatusList"
    ]
    """<p>The list of parameter statuses.</p>"""
    parameter_apply_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of updates to the parameters.</p>"""
    parameter_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the parameter group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterParameterGroup) -> dict:
    out: dict = {}
    if "cluster_parameter_status_list" in value:
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list

        out["ClusterParameterStatusList"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.serialize_json(
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
        import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list

        out["cluster_parameter_status_list"] = (
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_status_list.deserialize_json(
                data["ClusterParameterStatusList"]
            )
        )
    if "ParameterApplyStatus" in data:
        out["parameter_apply_status"] = data["ParameterApplyStatus"]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    return out
