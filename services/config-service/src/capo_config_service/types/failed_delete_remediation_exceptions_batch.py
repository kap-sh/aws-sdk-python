"""Generated from Smithy shape ``com.amazonaws.configservice#FailedDeleteRemediationExceptionsBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_exception_resource_keys
    import capo_config_service.types.string


class FailedDeleteRemediationExceptionsBatch(TypedDict, closed=True):
    failure_message: NotRequired["capo_config_service.types.string.String"]
    """<p>Returns a failure message for delete remediation exception. For example, Config creates an exception due to an internal error.</p>"""
    failed_items: NotRequired[
        "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
    ]
    """<p>Returns remediation exception resource key object of the failed items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedDeleteRemediationExceptionsBatch) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "failed_items" in value:
        import capo_config_service.types.remediation_exception_resource_keys

        out["FailedItems"] = (
            capo_config_service.types.remediation_exception_resource_keys.serialize_aws_json_1_1(
                value["failed_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedDeleteRemediationExceptionsBatch:
    out: FailedDeleteRemediationExceptionsBatch = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "FailedItems" in data:
        import capo_config_service.types.remediation_exception_resource_keys

        out["failed_items"] = (
            capo_config_service.types.remediation_exception_resource_keys.deserialize_aws_json_1_1(
                data["FailedItems"]
            )
        )
    return out
