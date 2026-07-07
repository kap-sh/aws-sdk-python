"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyUpdateProvisionedProductEngineWorkflowResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.engine_workflow_failure_reason
    import aws_sdk_service_catalog.types.engine_workflow_status
    import aws_sdk_service_catalog.types.engine_workflow_token
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token
    import aws_sdk_service_catalog.types.record_outputs


class NotifyUpdateProvisionedProductEngineWorkflowResultInput(TypedDict, closed=True):
    workflow_token: (
        "aws_sdk_service_catalog.types.engine_workflow_token.EngineWorkflowToken"
    )
    """<p> The encrypted contents of the update engine execution payload that Service Catalog sends after the Terraform product update workflow starts. </p>"""
    record_id: "aws_sdk_service_catalog.types.id.Id"
    """<p> The identifier of the record. </p>"""
    status: "aws_sdk_service_catalog.types.engine_workflow_status.EngineWorkflowStatus"
    """<p> The status of the update engine execution. </p>"""
    failure_reason: NotRequired[
        "aws_sdk_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
    ]
    """<p> The reason why the update engine execution failed. </p>"""
    outputs: NotRequired["aws_sdk_service_catalog.types.record_outputs.RecordOutputs"]
    """<p> The output of the update engine execution. </p>"""
    idempotency_token: (
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    )
    """<p> The idempotency token that identifies the update engine execution. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyUpdateProvisionedProductEngineWorkflowResultInput,
) -> dict:
    out: dict = {}
    out["WorkflowToken"] = value["workflow_token"]
    out["RecordId"] = value["record_id"]
    import aws_sdk_service_catalog.types.engine_workflow_status

    out["Status"] = (
        aws_sdk_service_catalog.types.engine_workflow_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "outputs" in value:
        import aws_sdk_service_catalog.types.record_outputs

        out["Outputs"] = (
            aws_sdk_service_catalog.types.record_outputs.serialize_aws_json_1_1(
                value["outputs"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyUpdateProvisionedProductEngineWorkflowResultInput:
    out: NotifyUpdateProvisionedProductEngineWorkflowResultInput = {}  # type: ignore[typeddict-item]
    if "WorkflowToken" in data:
        out["workflow_token"] = data["WorkflowToken"]
    else:
        raise DeserializationError(
            "NotifyUpdateProvisionedProductEngineWorkflowResultInput.workflow_token required"
        )
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError(
            "NotifyUpdateProvisionedProductEngineWorkflowResultInput.record_id required"
        )
    if "Status" in data:
        import aws_sdk_service_catalog.types.engine_workflow_status

        out["status"] = (
            aws_sdk_service_catalog.types.engine_workflow_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyUpdateProvisionedProductEngineWorkflowResultInput.status required"
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Outputs" in data:
        import aws_sdk_service_catalog.types.record_outputs

        out["outputs"] = (
            aws_sdk_service_catalog.types.record_outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "NotifyUpdateProvisionedProductEngineWorkflowResultInput.idempotency_token required"
        )
    return out
