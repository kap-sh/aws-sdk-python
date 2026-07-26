"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VPCOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.string_list


class VPCOptions(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_elasticsearch_service.types.string_list.StringList"]
    """<p>Specifies the subnets for VPC endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>Specifies the security groups for VPC endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VPCOptions) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_elasticsearch_service.types.string_list

        out["SubnetIds"] = capo_elasticsearch_service.types.string_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_elasticsearch_service.types.string_list

        out["SecurityGroupIds"] = (
            capo_elasticsearch_service.types.string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> VPCOptions:
    out: VPCOptions = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import capo_elasticsearch_service.types.string_list

        out["subnet_ids"] = (
            capo_elasticsearch_service.types.string_list.deserialize_json(
                data["SubnetIds"]
            )
        )
    if "SecurityGroupIds" in data:
        import capo_elasticsearch_service.types.string_list

        out["security_group_ids"] = (
            capo_elasticsearch_service.types.string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    return out
