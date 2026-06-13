"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceVpcConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.security_group_ids
    import aws_sdk_qbusiness.types.subnet_ids


class DataSourceVpcConfiguration(TypedDict):
    subnet_ids: "aws_sdk_qbusiness.types.subnet_ids.SubnetIds"
    """<p>A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.</p>"""
    security_group_ids: "aws_sdk_qbusiness.types.security_group_ids.SecurityGroupIds"
    """<p>A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Q Business to connect to the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceVpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.subnet_ids

    out["subnetIds"] = aws_sdk_qbusiness.types.subnet_ids.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_qbusiness.types.security_group_ids

    out["securityGroupIds"] = aws_sdk_qbusiness.types.security_group_ids.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> DataSourceVpcConfiguration:
    out: DataSourceVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_qbusiness.types.subnet_ids

        out["subnet_ids"] = aws_sdk_qbusiness.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("DataSourceVpcConfiguration.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_qbusiness.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_qbusiness.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "DataSourceVpcConfiguration.security_group_ids required"
        )
    return out
