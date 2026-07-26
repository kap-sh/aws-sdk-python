"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TunnelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.date_type
    import capo_iotsecuretunneling.types.description
    import capo_iotsecuretunneling.types.tunnel_arn
    import capo_iotsecuretunneling.types.tunnel_id
    import capo_iotsecuretunneling.types.tunnel_status


class TunnelSummary(TypedDict, closed=True):
    tunnel_id: NotRequired["capo_iotsecuretunneling.types.tunnel_id.TunnelId"]
    """<p>The unique alpha-numeric identifier for the tunnel.</p>"""
    tunnel_arn: NotRequired["capo_iotsecuretunneling.types.tunnel_arn.TunnelArn"]
    """<p>The Amazon Resource Name of the tunnel. </p>"""
    status: NotRequired["capo_iotsecuretunneling.types.tunnel_status.TunnelStatus"]
    """<p>The status of a tunnel. Valid values are: Open and Closed.</p>"""
    description: NotRequired["capo_iotsecuretunneling.types.description.Description"]
    """<p>A description of the tunnel.</p>"""
    created_at: NotRequired["capo_iotsecuretunneling.types.date_type.DateType"]
    """<p>The time the tunnel was created.</p>"""
    last_updated_at: NotRequired["capo_iotsecuretunneling.types.date_type.DateType"]
    """<p>The time the tunnel was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TunnelSummary) -> dict:
    out: dict = {}
    if "tunnel_id" in value:
        out["tunnelId"] = value["tunnel_id"]
    if "tunnel_arn" in value:
        out["tunnelArn"] = value["tunnel_arn"]
    if "status" in value:
        import capo_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            capo_iotsecuretunneling.types.tunnel_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_iotsecuretunneling.types.date_type

        out["createdAt"] = (
            capo_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_iotsecuretunneling.types.date_type

        out["lastUpdatedAt"] = (
            capo_iotsecuretunneling.types.date_type.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TunnelSummary:
    out: TunnelSummary = {}  # type: ignore[typeddict-item]
    if "tunnelId" in data:
        out["tunnel_id"] = data["tunnelId"]
    if "tunnelArn" in data:
        out["tunnel_arn"] = data["tunnelArn"]
    if "status" in data:
        import capo_iotsecuretunneling.types.tunnel_status

        out["status"] = (
            capo_iotsecuretunneling.types.tunnel_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_iotsecuretunneling.types.date_type

        out["created_at"] = (
            capo_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_iotsecuretunneling.types.date_type

        out["last_updated_at"] = (
            capo_iotsecuretunneling.types.date_type.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    return out
