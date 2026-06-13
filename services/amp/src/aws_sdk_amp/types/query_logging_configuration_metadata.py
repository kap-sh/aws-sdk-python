"""Generated from Smithy shape ``com.amazonaws.amp#QueryLoggingConfigurationMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_amp.types.logging_destinations
    import aws_sdk_amp.types.query_logging_configuration_status
    import aws_sdk_amp.types.workspace_id


class QueryLoggingConfigurationMetadata(TypedDict):
    status: "aws_sdk_amp.types.query_logging_configuration_status.QueryLoggingConfigurationStatus"
    """<p>The current status of the query logging configuration.</p>"""
    workspace: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace associated with this query logging configuration.</p>"""
    destinations: "aws_sdk_amp.types.logging_destinations.LoggingDestinations"
    """<p>The configured destinations for the query logging configuration.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the query logging configuration was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time when the query logging configuration was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLoggingConfigurationMetadata) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.query_logging_configuration_status

    out["status"] = aws_sdk_amp.types.query_logging_configuration_status.serialize_json(
        value["status"]
    )
    out["workspace"] = value["workspace"]
    import aws_sdk_amp.types.logging_destinations

    out["destinations"] = aws_sdk_amp.types.logging_destinations.serialize_json(
        value["destinations"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["createdAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_amp.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_amp.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    return out


def deserialize_json(data: dict) -> QueryLoggingConfigurationMetadata:
    out: QueryLoggingConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.query_logging_configuration_status

        out["status"] = (
            aws_sdk_amp.types.query_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("QueryLoggingConfigurationMetadata.status required")
    if "workspace" in data:
        out["workspace"] = data["workspace"]
    else:
        raise DeserializationError(
            "QueryLoggingConfigurationMetadata.workspace required"
        )
    if "destinations" in data:
        import aws_sdk_amp.types.logging_destinations

        out["destinations"] = aws_sdk_amp.types.logging_destinations.deserialize_json(
            data["destinations"]
        )
    else:
        raise DeserializationError(
            "QueryLoggingConfigurationMetadata.destinations required"
        )
    if "createdAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["created_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "QueryLoggingConfigurationMetadata.created_at required"
        )
    if "modifiedAt" in data:
        import aws_sdk_amp.types._prelude.timestamp

        out["modified_at"] = aws_sdk_amp.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError(
            "QueryLoggingConfigurationMetadata.modified_at required"
        )
    return out
