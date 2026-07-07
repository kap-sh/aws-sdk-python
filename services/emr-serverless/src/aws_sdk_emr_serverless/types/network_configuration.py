"""Generated from Smithy shape ``com.amazonaws.emrserverless#NetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.security_group_ids
    import aws_sdk_emr_serverless.types.subnet_ids


class NetworkConfiguration(TypedDict, closed=True):
    subnet_ids: NotRequired["aws_sdk_emr_serverless.types.subnet_ids.SubnetIds"]
    """<p>The array of subnet Ids for customer VPC connectivity.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_emr_serverless.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The array of security group Ids for customer VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_emr_serverless.types.subnet_ids

        out["subnetIds"] = aws_sdk_emr_serverless.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_emr_serverless.types.security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_emr_serverless.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_emr_serverless.types.subnet_ids

        out["subnet_ids"] = aws_sdk_emr_serverless.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_emr_serverless.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_emr_serverless.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
