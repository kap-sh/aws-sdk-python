"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.arn
    import aws_sdk_appfabric.types.ingestion_state
    import aws_sdk_appfabric.types.string255
    import aws_sdk_appfabric.types.tenant_identifier


class IngestionSummary(TypedDict):
    arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion.</p>"""
    app: "aws_sdk_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "aws_sdk_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    state: "aws_sdk_appfabric.types.ingestion_state.IngestionState"
    """<p>The status of the ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    import aws_sdk_appfabric.types.ingestion_state

    out["state"] = aws_sdk_appfabric.types.ingestion_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> IngestionSummary:
    out: IngestionSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestionSummary.arn required")
    if "app" in data:
        out["app"] = data["app"]
    else:
        raise DeserializationError("IngestionSummary.app required")
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    else:
        raise DeserializationError("IngestionSummary.tenant_id required")
    if "state" in data:
        import aws_sdk_appfabric.types.ingestion_state

        out["state"] = aws_sdk_appfabric.types.ingestion_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("IngestionSummary.state required")
    return out
