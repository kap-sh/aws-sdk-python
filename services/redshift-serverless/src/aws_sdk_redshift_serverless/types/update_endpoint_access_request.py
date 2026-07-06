"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.vpc_security_group_id_list


class UpdateEndpointAccessRequest(TypedDict, closed=True):
    endpoint_name: "str"
    """<p>The name of the VPC endpoint to update.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointAccessRequest) -> dict:
    out: dict = {}
    out["endpointName"] = value["endpoint_name"]
    if "vpc_security_group_ids" in value:
        import aws_sdk_redshift_serverless.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            aws_sdk_redshift_serverless.types.vpc_security_group_id_list.serialize_aws_json_1_1(
                value["vpc_security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointAccessRequest:
    out: UpdateEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "endpointName" in data:
        out["endpoint_name"] = data["endpointName"]
    else:
        raise DeserializationError("UpdateEndpointAccessRequest.endpoint_name required")
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_redshift_serverless.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_redshift_serverless.types.vpc_security_group_id_list.deserialize_aws_json_1_1(
                data["vpcSecurityGroupIds"]
            )
        )
    return out
