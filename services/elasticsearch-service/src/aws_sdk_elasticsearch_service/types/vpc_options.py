"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VPCOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.string_list


class VPCOptions(TypedDict):
    subnet_ids: NotRequired[
        "aws_sdk_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>Specifies the subnets for VPC endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>Specifies the security groups for VPC endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCOptions) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_elasticsearch_service.types.string_list

        out["SubnetIds"] = (
            aws_sdk_elasticsearch_service.types.string_list.serialize_json(
                value["subnet_ids"]
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


def deserialize_json(data: dict) -> VPCOptions:
    out: VPCOptions = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import aws_sdk_elasticsearch_service.types.string_list

        out["subnet_ids"] = (
            aws_sdk_elasticsearch_service.types.string_list.deserialize_json(
                data["SubnetIds"]
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
