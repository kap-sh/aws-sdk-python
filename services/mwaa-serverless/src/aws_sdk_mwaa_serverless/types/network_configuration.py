"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.security_group_ids
    import aws_sdk_mwaa_serverless.types.subnet_ids


class NetworkConfiguration(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_mwaa_serverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of VPC security group IDs to associate with the workflow execution environment.</p>"""
    subnet_ids: NotRequired["aws_sdk_mwaa_serverless.types.subnet_ids.SubnetIds"]
    """<p>A list of VPC subnet IDs where the workflow execution environment is deployed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_mwaa_serverless.types.security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_mwaa_serverless.types.security_group_ids.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_mwaa_serverless.types.subnet_ids

        out["SubnetIds"] = (
            aws_sdk_mwaa_serverless.types.subnet_ids.serialize_aws_json_1_0(
                value["subnet_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIds" in data:
        import aws_sdk_mwaa_serverless.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_mwaa_serverless.types.security_group_ids.deserialize_aws_json_1_0(
                data["SecurityGroupIds"]
            )
        )
    if "SubnetIds" in data:
        import aws_sdk_mwaa_serverless.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_mwaa_serverless.types.subnet_ids.deserialize_aws_json_1_0(
                data["SubnetIds"]
            )
        )
    return out
