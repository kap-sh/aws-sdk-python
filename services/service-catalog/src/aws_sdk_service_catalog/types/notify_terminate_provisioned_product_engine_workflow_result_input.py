"""Generated from Smithy shape ``com.amazonaws.servicecatalog#NotifyTerminateProvisionedProductEngineWorkflowResultInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.engine_workflow_failure_reason
    import aws_sdk_service_catalog.types.engine_workflow_status
    import aws_sdk_service_catalog.types.engine_workflow_token
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token


class NotifyTerminateProvisionedProductEngineWorkflowResultInput(TypedDict):
    workflow_token: (
        "aws_sdk_service_catalog.types.engine_workflow_token.EngineWorkflowToken"
    )
    """<p> The encrypted contents of the terminate engine execution payload that Service Catalog sends after the Terraform product terminate workflow starts. </p>"""
    record_id: "aws_sdk_service_catalog.types.id.Id"
    """<p> The identifier of the record. </p>"""
    status: "aws_sdk_service_catalog.types.engine_workflow_status.EngineWorkflowStatus"
    """<p> The status of the terminate engine execution. </p>"""
    failure_reason: NotRequired[
        "aws_sdk_service_catalog.types.engine_workflow_failure_reason.EngineWorkflowFailureReason"
    ]
    """<p> The reason why the terminate engine execution failed. </p>"""
    idempotency_token: (
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    )
    """<p> The idempotency token that identifies the terminate engine execution. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NotifyTerminateProvisionedProductEngineWorkflowResultInput,
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
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NotifyTerminateProvisionedProductEngineWorkflowResultInput:
    out: NotifyTerminateProvisionedProductEngineWorkflowResultInput = {}  # type: ignore[typeddict-item]
    if "WorkflowToken" in data:
        out["workflow_token"] = data["WorkflowToken"]
    else:
        raise DeserializationError(
            "NotifyTerminateProvisionedProductEngineWorkflowResultInput.workflow_token required"
        )
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError(
            "NotifyTerminateProvisionedProductEngineWorkflowResultInput.record_id required"
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
            "NotifyTerminateProvisionedProductEngineWorkflowResultInput.status required"
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "NotifyTerminateProvisionedProductEngineWorkflowResultInput.idempotency_token required"
        )
    return out
