"""Generated from Smithy shape ``com.amazonaws.configservice#PutRemediationExceptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.failed_remediation_exception_batches


class PutRemediationExceptionsResponse(TypedDict, closed=True):
    failed_batches: NotRequired[
        "capo_config_service.types.failed_remediation_exception_batches.FailedRemediationExceptionBatches"
    ]
    """<p>Returns a list of failed remediation exceptions batch objects. Each object in the batch consists of a list of failed items and failure messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRemediationExceptionsResponse) -> dict:
    out: dict = {}
    if "failed_batches" in value:
        import capo_config_service.types.failed_remediation_exception_batches

        out["FailedBatches"] = (
            capo_config_service.types.failed_remediation_exception_batches.serialize_aws_json_1_1(
                value["failed_batches"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRemediationExceptionsResponse:
    out: PutRemediationExceptionsResponse = {}  # type: ignore[typeddict-item]
    if "FailedBatches" in data:
        import capo_config_service.types.failed_remediation_exception_batches

        out["failed_batches"] = (
            capo_config_service.types.failed_remediation_exception_batches.deserialize_aws_json_1_1(
                data["FailedBatches"]
            )
        )
    return out
