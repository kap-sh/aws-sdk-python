"""Generated from Smithy shape ``com.amazonaws.configservice#StartRemediationExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_keys
    import aws_sdk_config_service.types.string


class StartRemediationExecutionResponse(TypedDict, closed=True):
    failure_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>Returns a failure message. For example, the resource is already compliant.</p>"""
    failed_items: NotRequired["aws_sdk_config_service.types.resource_keys.ResourceKeys"]
    """<p>For resources that have failed to start execution, the API returns a resource key object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemediationExecutionResponse) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "failed_items" in value:
        import aws_sdk_config_service.types.resource_keys

        out["FailedItems"] = (
            aws_sdk_config_service.types.resource_keys.serialize_aws_json_1_1(
                value["failed_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemediationExecutionResponse:
    out: StartRemediationExecutionResponse = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "FailedItems" in data:
        import aws_sdk_config_service.types.resource_keys

        out["failed_items"] = (
            aws_sdk_config_service.types.resource_keys.deserialize_aws_json_1_1(
                data["FailedItems"]
            )
        )
    return out
