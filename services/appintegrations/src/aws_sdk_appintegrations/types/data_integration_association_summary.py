"""Generated from Smithy shape ``com.amazonaws.appintegrations#DataIntegrationAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.client_id
    import aws_sdk_appintegrations.types.destination_uri
    import aws_sdk_appintegrations.types.execution_configuration
    import aws_sdk_appintegrations.types.last_execution_status


class DataIntegrationAssociationSummary(TypedDict, closed=True):
    data_integration_association_arn: NotRequired[
        "aws_sdk_appintegrations.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the DataIntegration association.</p>"""
    data_integration_arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the DataIntegration.</p>"""
    client_id: NotRequired["aws_sdk_appintegrations.types.client_id.ClientId"]
    """<p>The identifier for the client that is associated with the DataIntegration association.</p>"""
    destination_uri: NotRequired[
        "aws_sdk_appintegrations.types.destination_uri.DestinationURI"
    ]
    """<p>The URI of the data destination.</p>"""
    last_execution_status: NotRequired[
        "aws_sdk_appintegrations.types.last_execution_status.LastExecutionStatus"
    ]
    """<p>The execution status of the last job.</p>"""
    execution_configuration: NotRequired[
        "aws_sdk_appintegrations.types.execution_configuration.ExecutionConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationAssociationSummary) -> dict:
    out: dict = {}
    if "data_integration_association_arn" in value:
        out["DataIntegrationAssociationArn"] = value["data_integration_association_arn"]
    if "data_integration_arn" in value:
        out["DataIntegrationArn"] = value["data_integration_arn"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "destination_uri" in value:
        out["DestinationURI"] = value["destination_uri"]
    if "last_execution_status" in value:
        import aws_sdk_appintegrations.types.last_execution_status

        out["LastExecutionStatus"] = (
            aws_sdk_appintegrations.types.last_execution_status.serialize_json(
                value["last_execution_status"]
            )
        )
    if "execution_configuration" in value:
        import aws_sdk_appintegrations.types.execution_configuration

        out["ExecutionConfiguration"] = (
            aws_sdk_appintegrations.types.execution_configuration.serialize_json(
                value["execution_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationAssociationSummary:
    out: DataIntegrationAssociationSummary = {}  # type: ignore[typeddict-item]
    if "DataIntegrationAssociationArn" in data:
        out["data_integration_association_arn"] = data["DataIntegrationAssociationArn"]
    if "DataIntegrationArn" in data:
        out["data_integration_arn"] = data["DataIntegrationArn"]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "DestinationURI" in data:
        out["destination_uri"] = data["DestinationURI"]
    if "LastExecutionStatus" in data:
        import aws_sdk_appintegrations.types.last_execution_status

        out["last_execution_status"] = (
            aws_sdk_appintegrations.types.last_execution_status.deserialize_json(
                data["LastExecutionStatus"]
            )
        )
    if "ExecutionConfiguration" in data:
        import aws_sdk_appintegrations.types.execution_configuration

        out["execution_configuration"] = (
            aws_sdk_appintegrations.types.execution_configuration.deserialize_json(
                data["ExecutionConfiguration"]
            )
        )
    return out
