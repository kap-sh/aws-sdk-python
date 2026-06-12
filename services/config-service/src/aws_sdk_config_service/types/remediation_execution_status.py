"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.remediation_execution_state
    import aws_sdk_config_service.types.remediation_execution_steps
    import aws_sdk_config_service.types.resource_key


class RemediationExecutionStatus(TypedDict):
    resource_key: NotRequired["aws_sdk_config_service.types.resource_key.ResourceKey"]
    state: NotRequired[
        "aws_sdk_config_service.types.remediation_execution_state.RemediationExecutionState"
    ]
    """<p>ENUM of the values.</p>"""
    step_details: NotRequired[
        "aws_sdk_config_service.types.remediation_execution_steps.RemediationExecutionSteps"
    ]
    """<p>Details of every step.</p>"""
    invocation_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>Start time when the remediation was executed.</p>"""
    last_updated_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time when the remediation execution was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionStatus) -> dict:
    out: dict = {}
    if "resource_key" in value:
        import aws_sdk_config_service.types.resource_key

        out["ResourceKey"] = (
            aws_sdk_config_service.types.resource_key.serialize_aws_json_1_1(
                value["resource_key"]
            )
        )
    if "state" in value:
        import aws_sdk_config_service.types.remediation_execution_state

        out["State"] = (
            aws_sdk_config_service.types.remediation_execution_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "step_details" in value:
        import aws_sdk_config_service.types.remediation_execution_steps

        out["StepDetails"] = (
            aws_sdk_config_service.types.remediation_execution_steps.serialize_aws_json_1_1(
                value["step_details"]
            )
        )
    if "invocation_time" in value:
        import aws_sdk_config_service.types.date

        out["InvocationTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["invocation_time"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdatedTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationExecutionStatus:
    out: RemediationExecutionStatus = {}  # type: ignore[typeddict-item]
    if "ResourceKey" in data:
        import aws_sdk_config_service.types.resource_key

        out["resource_key"] = (
            aws_sdk_config_service.types.resource_key.deserialize_aws_json_1_1(
                data["ResourceKey"]
            )
        )
    if "State" in data:
        import aws_sdk_config_service.types.remediation_execution_state

        out["state"] = (
            aws_sdk_config_service.types.remediation_execution_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StepDetails" in data:
        import aws_sdk_config_service.types.remediation_execution_steps

        out["step_details"] = (
            aws_sdk_config_service.types.remediation_execution_steps.deserialize_aws_json_1_1(
                data["StepDetails"]
            )
        )
    if "InvocationTime" in data:
        import aws_sdk_config_service.types.date

        out["invocation_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["InvocationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_config_service.types.date

        out["last_updated_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
