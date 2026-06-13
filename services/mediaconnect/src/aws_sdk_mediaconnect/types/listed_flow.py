"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedFlow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.maintenance
    import aws_sdk_mediaconnect.types.source_type
    import aws_sdk_mediaconnect.types.status


class ListedFlow(TypedDict):
    availability_zone: NotRequired["str"]
    """<p> The Availability Zone that the flow was created in.</p>"""
    description: NotRequired["str"]
    """<p> A description of the flow.</p>"""
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow.</p>"""
    name: NotRequired["str"]
    """<p> The name of the flow.</p>"""
    source_type: NotRequired["aws_sdk_mediaconnect.types.source_type.SourceType"]
    """<p> The type of source. This value is either owned (originated somewhere other than an MediaConnect flow owned by another Amazon Web Services account) or entitled (originated at a MediaConnect flow owned by another Amazon Web Services account).</p>"""
    status: NotRequired["aws_sdk_mediaconnect.types.status.Status"]
    """<p> The current status of the flow.</p>"""
    maintenance: NotRequired["aws_sdk_mediaconnect.types.maintenance.Maintenance"]
    """<p> The maintenance settings for the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedFlow) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "description" in value:
        out["description"] = value["description"]
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "source_type" in value:
        import aws_sdk_mediaconnect.types.source_type

        out["sourceType"] = aws_sdk_mediaconnect.types.source_type.serialize_json(
            value["source_type"]
        )
    if "status" in value:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.serialize_json(
            value["status"]
        )
    if "maintenance" in value:
        import aws_sdk_mediaconnect.types.maintenance

        out["maintenance"] = aws_sdk_mediaconnect.types.maintenance.serialize_json(
            value["maintenance"]
        )
    return out


def deserialize_json(data: dict) -> ListedFlow:
    out: ListedFlow = {}  # type: ignore[typeddict-item]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "description" in data:
        out["description"] = data["description"]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "sourceType" in data:
        import aws_sdk_mediaconnect.types.source_type

        out["source_type"] = aws_sdk_mediaconnect.types.source_type.deserialize_json(
            data["sourceType"]
        )
    if "status" in data:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.deserialize_json(
            data["status"]
        )
    if "maintenance" in data:
        import aws_sdk_mediaconnect.types.maintenance

        out["maintenance"] = aws_sdk_mediaconnect.types.maintenance.deserialize_json(
            data["maintenance"]
        )
    return out
