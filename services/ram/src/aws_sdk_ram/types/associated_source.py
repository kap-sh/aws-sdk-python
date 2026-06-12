"""Generated from Smithy shape ``com.amazonaws.ram#AssociatedSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.string


class AssociatedSource(TypedDict):
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource share that contains the source association.</p>"""
    source_id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The identifier of the source. This can be an account ID, Amazon Resource Name (ARN), organization ID, or organization path.</p>"""
    source_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The type of source.</p>"""
    status: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The current status of the source association.</p>"""
    last_updated_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the source association was last updated.</p>"""
    creation_time: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the source association was created.</p>"""
    status_message: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>A message about the status of the source association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSource) -> dict:
    out: dict = {}
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "source_type" in value:
        out["sourceType"] = value["source_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "last_updated_time" in value:
        import aws_sdk_ram.types.date_time

        out["lastUpdatedTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["last_updated_time"]
        )
    if "creation_time" in value:
        import aws_sdk_ram.types.date_time

        out["creationTime"] = aws_sdk_ram.types.date_time.serialize_json(
            value["creation_time"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> AssociatedSource:
    out: AssociatedSource = {}  # type: ignore[typeddict-item]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "sourceType" in data:
        out["source_type"] = data["sourceType"]
    if "status" in data:
        out["status"] = data["status"]
    if "lastUpdatedTime" in data:
        import aws_sdk_ram.types.date_time

        out["last_updated_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "creationTime" in data:
        import aws_sdk_ram.types.date_time

        out["creation_time"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["creationTime"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
