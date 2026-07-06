"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceVpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.security_group_id_list
    import aws_sdk_kendra.types.subnet_id_list


class DataSourceVpcConfiguration(TypedDict, closed=True):
    subnet_ids: "aws_sdk_kendra.types.subnet_id_list.SubnetIdList"
    """<p>A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.</p>"""
    security_group_ids: (
        "aws_sdk_kendra.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceVpcConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.subnet_id_list

    out["SubnetIds"] = aws_sdk_kendra.types.subnet_id_list.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    import aws_sdk_kendra.types.security_group_id_list

    out["SecurityGroupIds"] = (
        aws_sdk_kendra.types.security_group_id_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceVpcConfiguration:
    out: DataSourceVpcConfiguration = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_kendra.types.subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_kendra.types.subnet_id_list.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        raise DeserializationError("DataSourceVpcConfiguration.subnet_ids required")
    if "SecurityGroupIds" in data:
        import aws_sdk_kendra.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_kendra.types.security_group_id_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "DataSourceVpcConfiguration.security_group_ids required"
        )
    return out
