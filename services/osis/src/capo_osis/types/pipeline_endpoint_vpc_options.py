"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointVpcOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.security_group_ids
    import capo_osis.types.subnet_ids


class PipelineEndpointVpcOptions(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_osis.types.subnet_ids.SubnetIds"]
    """<p>A list of subnet IDs where the pipeline endpoint network interfaces are created.</p>"""
    security_group_ids: NotRequired[
        "capo_osis.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of security group IDs that control network access to the pipeline endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointVpcOptions) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_osis.types.subnet_ids

        out["SubnetIds"] = capo_osis.types.subnet_ids.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_osis.types.security_group_ids

        out["SecurityGroupIds"] = capo_osis.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    return out


def deserialize_json(data: dict) -> PipelineEndpointVpcOptions:
    out: PipelineEndpointVpcOptions = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import capo_osis.types.subnet_ids

        out["subnet_ids"] = capo_osis.types.subnet_ids.deserialize_json(
            data["SubnetIds"]
        )
    if "SecurityGroupIds" in data:
        import capo_osis.types.security_group_ids

        out["security_group_ids"] = capo_osis.types.security_group_ids.deserialize_json(
            data["SecurityGroupIds"]
        )
    return out
