"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceConnectionDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.last_sync
    import aws_sdk_service_catalog.types.source_connection_parameters
    import aws_sdk_service_catalog.types.source_type


class SourceConnectionDetail(TypedDict):
    type: NotRequired["aws_sdk_service_catalog.types.source_type.SourceType"]
    """<p>The only supported <code>SourceConnection</code> type is Codestar.</p>"""
    connection_parameters: NotRequired[
        "aws_sdk_service_catalog.types.source_connection_parameters.SourceConnectionParameters"
    ]
    """<p>The connection details based on the connection <code>Type</code>.</p>"""
    last_sync: NotRequired["aws_sdk_service_catalog.types.last_sync.LastSync"]
    """<p>Provides details about the product's connection sync and contains the following sub-fields. </p> <ul> <li> <p> <code>LastSyncTime</code> </p> </li> <li> <p> <code>LastSyncStatus</code> </p> </li> <li> <p> <code>LastSyncStatusMessage</code> </p> </li> <li> <p> <code>LastSuccessfulSyncTime</code> </p> </li> <li> <p> <code>LastSuccessfulSyncProvisioningArtifactID</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConnectionDetail) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_service_catalog.types.source_type

        out["Type"] = aws_sdk_service_catalog.types.source_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "connection_parameters" in value:
        import aws_sdk_service_catalog.types.source_connection_parameters

        out["ConnectionParameters"] = (
            aws_sdk_service_catalog.types.source_connection_parameters.serialize_aws_json_1_1(
                value["connection_parameters"]
            )
        )
    if "last_sync" in value:
        import aws_sdk_service_catalog.types.last_sync

        out["LastSync"] = (
            aws_sdk_service_catalog.types.last_sync.serialize_aws_json_1_1(
                value["last_sync"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConnectionDetail:
    out: SourceConnectionDetail = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_service_catalog.types.source_type

        out["type"] = (
            aws_sdk_service_catalog.types.source_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "ConnectionParameters" in data:
        import aws_sdk_service_catalog.types.source_connection_parameters

        out["connection_parameters"] = (
            aws_sdk_service_catalog.types.source_connection_parameters.deserialize_aws_json_1_1(
                data["ConnectionParameters"]
            )
        )
    if "LastSync" in data:
        import aws_sdk_service_catalog.types.last_sync

        out["last_sync"] = (
            aws_sdk_service_catalog.types.last_sync.deserialize_aws_json_1_1(
                data["LastSync"]
            )
        )
    return out
