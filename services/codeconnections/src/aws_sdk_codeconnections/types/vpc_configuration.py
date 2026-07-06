"""Generated from Smithy shape ``com.amazonaws.codeconnections#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.security_group_ids
    import aws_sdk_codeconnections.types.subnet_ids
    import aws_sdk_codeconnections.types.tls_certificate
    import aws_sdk_codeconnections.types.vpc_id


class VpcConfiguration(TypedDict, closed=True):
    vpc_id: "aws_sdk_codeconnections.types.vpc_id.VpcId"
    """<p>The ID of the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    subnet_ids: "aws_sdk_codeconnections.types.subnet_ids.SubnetIds"
    """<p>The ID of the subnet or subnets associated with the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    security_group_ids: (
        "aws_sdk_codeconnections.types.security_group_ids.SecurityGroupIds"
    )
    """<p>The ID of the security group or security groups associated with the Amazon VPC connected to the infrastructure where your provider type is installed.</p>"""
    tls_certificate: NotRequired[
        "aws_sdk_codeconnections.types.tls_certificate.TlsCertificate"
    ]
    """<p>The value of the Transport Layer Security (TLS) certificate associated with the infrastructure where your provider type is installed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcConfiguration) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import aws_sdk_codeconnections.types.subnet_ids

    out["SubnetIds"] = aws_sdk_codeconnections.types.subnet_ids.serialize_aws_json_1_0(
        value["subnet_ids"]
    )
    import aws_sdk_codeconnections.types.security_group_ids

    out["SecurityGroupIds"] = (
        aws_sdk_codeconnections.types.security_group_ids.serialize_aws_json_1_0(
            value["security_group_ids"]
        )
    )
    if "tls_certificate" in value:
        out["TlsCertificate"] = value["tls_certificate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("VpcConfiguration.vpc_id required")
    if "SubnetIds" in data:
        import aws_sdk_codeconnections.types.subnet_ids

        out["subnet_ids"] = (
            aws_sdk_codeconnections.types.subnet_ids.deserialize_aws_json_1_0(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_codeconnections.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_codeconnections.types.security_group_ids.deserialize_aws_json_1_0(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("VpcConfiguration.security_group_ids required")
    if "TlsCertificate" in data:
        out["tls_certificate"] = data["TlsCertificate"]
    return out
