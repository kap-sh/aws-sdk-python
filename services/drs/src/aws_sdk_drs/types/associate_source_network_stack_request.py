"""Generated from Smithy shape ``com.amazonaws.drs#AssociateSourceNetworkStackRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.cfn_stack_name
    import aws_sdk_drs.types.source_network_id


class AssociateSourceNetworkStackRequest(TypedDict):
    source_network_id: "aws_sdk_drs.types.source_network_id.SourceNetworkID"
    """<p>The Source Network ID to associate with CloudFormation template.</p>"""
    cfn_stack_name: "aws_sdk_drs.types.cfn_stack_name.CfnStackName"
    """<p>CloudFormation template to associate with a Source Network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSourceNetworkStackRequest) -> dict:
    out: dict = {}
    out["sourceNetworkID"] = value["source_network_id"]
    out["cfnStackName"] = value["cfn_stack_name"]
    return out


def deserialize_json(data: dict) -> AssociateSourceNetworkStackRequest:
    out: AssociateSourceNetworkStackRequest = {}  # type: ignore[typeddict-item]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    else:
        raise DeserializationError(
            "AssociateSourceNetworkStackRequest.source_network_id required"
        )
    if "cfnStackName" in data:
        out["cfn_stack_name"] = data["cfnStackName"]
    else:
        raise DeserializationError(
            "AssociateSourceNetworkStackRequest.cfn_stack_name required"
        )
    return out
