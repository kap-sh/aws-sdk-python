"""Generated from Smithy shape ``com.amazonaws.configservice#FailedRemediationExceptionBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_exceptions
    import capo_config_service.types.string


class FailedRemediationExceptionBatch(TypedDict, closed=True):
    failure_message: NotRequired["capo_config_service.types.string.String"]
    """<p>Returns a failure message. For example, the auto-remediation has failed.</p>"""
    failed_items: NotRequired[
        "capo_config_service.types.remediation_exceptions.RemediationExceptions"
    ]
    """<p>Returns remediation exception resource key object of the failed items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRemediationExceptionBatch) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "failed_items" in value:
        import capo_config_service.types.remediation_exceptions

        out["FailedItems"] = (
            capo_config_service.types.remediation_exceptions.serialize_aws_json_1_1(
                value["failed_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedRemediationExceptionBatch:
    out: FailedRemediationExceptionBatch = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "FailedItems" in data:
        import capo_config_service.types.remediation_exceptions

        out["failed_items"] = (
            capo_config_service.types.remediation_exceptions.deserialize_aws_json_1_1(
                data["FailedItems"]
            )
        )
    return out
