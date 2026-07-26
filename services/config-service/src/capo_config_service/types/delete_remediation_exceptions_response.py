"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRemediationExceptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.failed_delete_remediation_exceptions_batches


class DeleteRemediationExceptionsResponse(TypedDict, closed=True):
    failed_batches: NotRequired[
        "capo_config_service.types.failed_delete_remediation_exceptions_batches.FailedDeleteRemediationExceptionsBatches"
    ]
    """<p>Returns a list of failed delete remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRemediationExceptionsResponse) -> dict:
    out: dict = {}
    if "failed_batches" in value:
        import capo_config_service.types.failed_delete_remediation_exceptions_batches

        out["FailedBatches"] = (
            capo_config_service.types.failed_delete_remediation_exceptions_batches.serialize_aws_json_1_1(
                value["failed_batches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRemediationExceptionsResponse:
    out: DeleteRemediationExceptionsResponse = {}  # type: ignore[typeddict-item]
    if "FailedBatches" in data:
        import capo_config_service.types.failed_delete_remediation_exceptions_batches

        out["failed_batches"] = (
            capo_config_service.types.failed_delete_remediation_exceptions_batches.deserialize_aws_json_1_1(
                data["FailedBatches"]
            )
        )
    return out
