"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkInstanceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_lcm_op_occ_id
    import aws_sdk_tnb.types.tag_map


class UpdateSolNetworkInstanceOutput(TypedDict):
    ns_lcm_op_occ_id: NotRequired["aws_sdk_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"]
    """<p>The identifier of the network operation.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkInstanceOutput) -> dict:
    out: dict = {}
    if "ns_lcm_op_occ_id" in value:
        out["nsLcmOpOccId"] = value["ns_lcm_op_occ_id"]
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateSolNetworkInstanceOutput:
    out: UpdateSolNetworkInstanceOutput = {}  # type: ignore[typeddict-item]
    if "nsLcmOpOccId" in data:
        out["ns_lcm_op_occ_id"] = data["nsLcmOpOccId"]
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out
