"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VPCDerivedInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.string
    import aws_sdk_elasticsearch_service.types.string_list


class VPCDerivedInfo(TypedDict):
    vpc_id: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]
    """<p>The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>Specifies the subnets for VPC endpoint.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>Specifies the security groups for VPC endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCDerivedInfo) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_elasticsearch_service.types.string_list

        out["SubnetIds"] = (
            aws_sdk_elasticsearch_service.types.string_list.serialize_json(
                value["subnet_ids"]
            )
        )
    if "availability_zones" in value:
        import aws_sdk_elasticsearch_service.types.string_list

        out["AvailabilityZones"] = (
            aws_sdk_elasticsearch_service.types.string_list.serialize_json(
                value["availability_zones"]
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_elasticsearch_service.types.string_list

        out["SecurityGroupIds"] = (
            aws_sdk_elasticsearch_service.types.string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> VPCDerivedInfo:
    out: VPCDerivedInfo = {}  # type: ignore[typeddict-item]
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    if "SubnetIds" in data:
        import aws_sdk_elasticsearch_service.types.string_list

        out["subnet_ids"] = (
            aws_sdk_elasticsearch_service.types.string_list.deserialize_json(
                data["SubnetIds"]
            )
        )
    if "AvailabilityZones" in data:
        import aws_sdk_elasticsearch_service.types.string_list

        out["availability_zones"] = (
            aws_sdk_elasticsearch_service.types.string_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    if "SecurityGroupIds" in data:
        import aws_sdk_elasticsearch_service.types.string_list

        out["security_group_ids"] = (
            aws_sdk_elasticsearch_service.types.string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    return out
