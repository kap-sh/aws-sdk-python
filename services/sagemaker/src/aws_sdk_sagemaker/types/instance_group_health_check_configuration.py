"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupHealthCheckConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.deep_health_checks
    import aws_sdk_sagemaker.types.instance_ids


class InstanceGroupHealthCheckConfiguration(TypedDict):
    instance_group_name: (
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group.</p>"""
    instance_ids: NotRequired["aws_sdk_sagemaker.types.instance_ids.InstanceIds"]
    """<p>A list of Amazon Elastic Compute Cloud (EC2) instance IDs on which to perform deep health checks.</p> <note> <p>Leave this field blank to perform deep health checks on the entire instance group.</p> </note>"""
    deep_health_checks: "aws_sdk_sagemaker.types.deep_health_checks.DeepHealthChecks"
    """<p>A list of deep health checks to be performed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupHealthCheckConfiguration) -> dict:
    out: dict = {}
    out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_ids" in value:
        import aws_sdk_sagemaker.types.instance_ids

        out["InstanceIds"] = (
            aws_sdk_sagemaker.types.instance_ids.serialize_aws_json_1_1(
                value["instance_ids"]
            )
        )
    import aws_sdk_sagemaker.types.deep_health_checks

    out["DeepHealthChecks"] = (
        aws_sdk_sagemaker.types.deep_health_checks.serialize_aws_json_1_1(
            value["deep_health_checks"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupHealthCheckConfiguration:
    out: InstanceGroupHealthCheckConfiguration = {}  # type: ignore[typeddict-item]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        raise DeserializationError(
            "InstanceGroupHealthCheckConfiguration.instance_group_name required"
        )
    if "InstanceIds" in data:
        import aws_sdk_sagemaker.types.instance_ids

        out["instance_ids"] = (
            aws_sdk_sagemaker.types.instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    if "DeepHealthChecks" in data:
        import aws_sdk_sagemaker.types.deep_health_checks

        out["deep_health_checks"] = (
            aws_sdk_sagemaker.types.deep_health_checks.deserialize_aws_json_1_1(
                data["DeepHealthChecks"]
            )
        )
    else:
        raise DeserializationError(
            "InstanceGroupHealthCheckConfiguration.deep_health_checks required"
        )
    return out
