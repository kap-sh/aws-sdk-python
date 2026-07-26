"""Generated from Smithy shape ``com.amazonaws.configservice#FailedRemediationBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_configurations
    import capo_config_service.types.string


class FailedRemediationBatch(TypedDict, closed=True):
    failure_message: NotRequired["capo_config_service.types.string.String"]
    """<p>Returns a failure message. For example, the resource is already compliant.</p>"""
    failed_items: NotRequired[
        "capo_config_service.types.remediation_configurations.RemediationConfigurations"
    ]
    """<p>Returns remediation configurations of the failed items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRemediationBatch) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "failed_items" in value:
        import capo_config_service.types.remediation_configurations

        out["FailedItems"] = (
            capo_config_service.types.remediation_configurations.serialize_aws_json_1_1(
                value["failed_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedRemediationBatch:
    out: FailedRemediationBatch = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "FailedItems" in data:
        import capo_config_service.types.remediation_configurations

        out["failed_items"] = (
            capo_config_service.types.remediation_configurations.deserialize_aws_json_1_1(
                data["FailedItems"]
            )
        )
    return out
