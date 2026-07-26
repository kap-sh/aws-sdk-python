"""Generated from Smithy shape ``com.amazonaws.opensearch#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_name
    import capo_opensearch.types.application_status
    import capo_opensearch.types.arn
    import capo_opensearch.types.id
    import capo_opensearch.types.string
    import capo_opensearch.types.timestamp


class ApplicationSummary(TypedDict, closed=True):
    id: NotRequired["capo_opensearch.types.id.Id"]
    """<p>The unique identifier of an OpenSearch application.</p>"""
    arn: NotRequired["capo_opensearch.types.arn.ARN"]
    name: NotRequired["capo_opensearch.types.application_name.ApplicationName"]
    """<p>The name of an OpenSearch application.</p>"""
    endpoint: NotRequired["capo_opensearch.types.string.String"]
    """<p>The endpoint URL of an OpenSearch application.</p>"""
    status: NotRequired["capo_opensearch.types.application_status.ApplicationStatus"]
    """<p>The current status of an OpenSearch application. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>"""
    created_at: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp when an OpenSearch application was created.</p>"""
    last_updated_at: NotRequired["capo_opensearch.types.timestamp.Timestamp"]
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
        import capo_opensearch.types.application_status

        out["status"] = capo_opensearch.types.application_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_opensearch.types.timestamp

        out["createdAt"] = capo_opensearch.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_opensearch.types.timestamp

        out["lastUpdatedAt"] = capo_opensearch.types.timestamp.serialize_json(
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
        import capo_opensearch.types.application_status

        out["status"] = capo_opensearch.types.application_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import capo_opensearch.types.timestamp

        out["created_at"] = capo_opensearch.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_opensearch.types.timestamp

        out["last_updated_at"] = capo_opensearch.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
