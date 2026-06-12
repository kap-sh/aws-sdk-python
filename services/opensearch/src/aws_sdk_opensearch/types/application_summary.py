"""Generated from Smithy shape ``com.amazonaws.opensearch#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.application_name
    import aws_sdk_opensearch.types.application_status
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.id
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.timestamp


class ApplicationSummary(TypedDict):
    id: NotRequired["aws_sdk_opensearch.types.id.Id"]
    """<p>The unique identifier of an OpenSearch application.</p>"""
    arn: NotRequired["aws_sdk_opensearch.types.arn.ARN"]
    name: NotRequired["aws_sdk_opensearch.types.application_name.ApplicationName"]
    """<p>The name of an OpenSearch application.</p>"""
    endpoint: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The endpoint URL of an OpenSearch application.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.application_status.ApplicationStatus"]
    """<p>The current status of an OpenSearch application. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp when an OpenSearch application was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp of the last update to an OpenSearch application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "status" in value:
        import aws_sdk_opensearch.types.application_status

        out["status"] = aws_sdk_opensearch.types.application_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_opensearch.types.timestamp

        out["createdAt"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_opensearch.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "status" in data:
        import aws_sdk_opensearch.types.application_status

        out["status"] = aws_sdk_opensearch.types.application_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_opensearch.types.timestamp

        out["created_at"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_opensearch.types.timestamp

        out["last_updated_at"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
