"""Generated from Smithy shape ``com.amazonaws.appfabric#Ingestion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.arn
    import aws_sdk_appfabric.types.date_time
    import aws_sdk_appfabric.types.ingestion_state
    import aws_sdk_appfabric.types.ingestion_type
    import aws_sdk_appfabric.types.string255
    import aws_sdk_appfabric.types.tenant_identifier


class Ingestion(TypedDict, closed=True):
    arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion.</p>"""
    app_bundle_arn: "aws_sdk_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle for the ingestion.</p>"""
    app: "aws_sdk_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "aws_sdk_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    created_at: "aws_sdk_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the ingestion was created.</p>"""
    updated_at: "aws_sdk_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the ingestion was last updated.</p>"""
    state: "aws_sdk_appfabric.types.ingestion_state.IngestionState"
    """<p>The status of the ingestion.</p>"""
    ingestion_type: "aws_sdk_appfabric.types.ingestion_type.IngestionType"
    """<p>The type of the ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ingestion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["appBundleArn"] = value["app_bundle_arn"]
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    import aws_sdk_appfabric.types.date_time

    out["createdAt"] = aws_sdk_appfabric.types.date_time.serialize_json(
        value["created_at"]
    )
    import aws_sdk_appfabric.types.date_time

    out["updatedAt"] = aws_sdk_appfabric.types.date_time.serialize_json(
        value["updated_at"]
    )
    import aws_sdk_appfabric.types.ingestion_state

    out["state"] = aws_sdk_appfabric.types.ingestion_state.serialize_json(
        value["state"]
    )
    import aws_sdk_appfabric.types.ingestion_type

    out["ingestionType"] = aws_sdk_appfabric.types.ingestion_type.serialize_json(
        value["ingestion_type"]
    )
    return out


def deserialize_json(data: dict) -> Ingestion:
    out: Ingestion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Ingestion.arn required")
    if "appBundleArn" in data:
        out["app_bundle_arn"] = data["appBundleArn"]
    else:
        raise DeserializationError("Ingestion.app_bundle_arn required")
    if "app" in data:
        out["app"] = data["app"]
    else:
        raise DeserializationError("Ingestion.app required")
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    else:
        raise DeserializationError("Ingestion.tenant_id required")
    if "createdAt" in data:
        import aws_sdk_appfabric.types.date_time

        out["created_at"] = aws_sdk_appfabric.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Ingestion.created_at required")
    if "updatedAt" in data:
        import aws_sdk_appfabric.types.date_time

        out["updated_at"] = aws_sdk_appfabric.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Ingestion.updated_at required")
    if "state" in data:
        import aws_sdk_appfabric.types.ingestion_state

        out["state"] = aws_sdk_appfabric.types.ingestion_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("Ingestion.state required")
    if "ingestionType" in data:
        import aws_sdk_appfabric.types.ingestion_type

        out["ingestion_type"] = aws_sdk_appfabric.types.ingestion_type.deserialize_json(
            data["ingestionType"]
        )
    else:
        raise DeserializationError("Ingestion.ingestion_type required")
    return out
