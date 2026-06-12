"""Generated from Smithy shape ``com.amazonaws.tnb#CreateSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_tnb.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_arn
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.tag_map

class CreateSolNetworkInstanceOutput(TypedDict):
    id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""
    arn: "aws_sdk_tnb.types.ns_instance_arn.NsInstanceArn"
    """<p>Network instance ARN.</p>"""
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>Network service descriptor ID.</p>"""
    ns_instance_name: "str"
    """<p>Network instance name.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["nsdInfoId"] = value["nsd_info_id"]
    out["nsInstanceName"] = value["ns_instance_name"]
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map
        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSolNetworkInstanceOutput:
    out: CreateSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceOutput.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceOutput.arn required")
    if "nsdInfoId" in data:
        out["nsd_info_id"] = data["nsdInfoId"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceOutput.nsd_info_id required")
    if "nsInstanceName" in data:
        out["ns_instance_name"] = data["nsInstanceName"]
    else:
        raise DeserializationError("CreateSolNetworkInstanceOutput.ns_instance_name required")
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map
        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out