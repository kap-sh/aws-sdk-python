"""Generated from Smithy shape ``com.amazonaws.ssm#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.node_capture_time
    import aws_sdk_ssm.types.node_id
    import aws_sdk_ssm.types.node_owner_info
    import aws_sdk_ssm.types.node_region
    import aws_sdk_ssm.types.node_type


class Node(TypedDict, closed=True):
    capture_time: NotRequired["aws_sdk_ssm.types.node_capture_time.NodeCaptureTime"]
    """<p>The UTC timestamp for when the managed node data was last captured.</p>"""
    id: NotRequired["aws_sdk_ssm.types.node_id.NodeId"]
    """<p>The ID of the managed node.</p>"""
    owner: NotRequired["aws_sdk_ssm.types.node_owner_info.NodeOwnerInfo"]
    """<p>Information about the ownership of the managed node.</p>"""
    region: NotRequired["aws_sdk_ssm.types.node_region.NodeRegion"]
    """<p>The Amazon Web Services Region that a managed node was created in or assigned to.</p>"""
    node_type: NotRequired["aws_sdk_ssm.types.node_type.NodeType"]
    """<p>Information about the type of node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "capture_time" in value:
        import aws_sdk_ssm.types.node_capture_time

        out["CaptureTime"] = aws_sdk_ssm.types.node_capture_time.serialize_aws_json_1_1(
            value["capture_time"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "owner" in value:
        import aws_sdk_ssm.types.node_owner_info

        out["Owner"] = aws_sdk_ssm.types.node_owner_info.serialize_aws_json_1_1(
            value["owner"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    if "node_type" in value:
        import aws_sdk_ssm.types.node_type

        out["NodeType"] = aws_sdk_ssm.types.node_type.serialize_aws_json_1_1(
            value["node_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if "CaptureTime" in data:
        import aws_sdk_ssm.types.node_capture_time

        out["capture_time"] = (
            aws_sdk_ssm.types.node_capture_time.deserialize_aws_json_1_1(
                data["CaptureTime"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Owner" in data:
        import aws_sdk_ssm.types.node_owner_info

        out["owner"] = aws_sdk_ssm.types.node_owner_info.deserialize_aws_json_1_1(
            data["Owner"]
        )
    if "Region" in data:
        out["region"] = data["Region"]
    if "NodeType" in data:
        import aws_sdk_ssm.types.node_type

        out["node_type"] = aws_sdk_ssm.types.node_type.deserialize_aws_json_1_1(
            data["NodeType"]
        )
    return out
