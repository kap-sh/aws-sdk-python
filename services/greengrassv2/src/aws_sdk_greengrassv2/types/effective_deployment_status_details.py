"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.effective_deployment_error_stack
    import aws_sdk_greengrassv2.types.effective_deployment_error_type_list


class EffectiveDeploymentStatusDetails(TypedDict, closed=True):
    error_stack: NotRequired[
        "aws_sdk_greengrassv2.types.effective_deployment_error_stack.EffectiveDeploymentErrorStack"
    ]
    """<p>Contains an ordered list of short error codes that range from the most generic error to the most specific one. The error codes describe the reason for failure whenever the <code>coreDeviceExecutionStatus</code> is in a failed state. The response will be an empty list if there is no error.</p>"""
    error_types: NotRequired[
        "aws_sdk_greengrassv2.types.effective_deployment_error_type_list.EffectiveDeploymentErrorTypeList"
    ]
    """<p>Contains tags which describe the error. You can use the error types to classify errors to assist with remediating the failure. The response will be an empty list if there is no error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentStatusDetails) -> dict:
    out: dict = {}
    if "error_stack" in value:
        import aws_sdk_greengrassv2.types.effective_deployment_error_stack

        out["errorStack"] = (
            aws_sdk_greengrassv2.types.effective_deployment_error_stack.serialize_json(
                value["error_stack"]
            )
        )
    if "error_types" in value:
        import aws_sdk_greengrassv2.types.effective_deployment_error_type_list

        out["errorTypes"] = (
            aws_sdk_greengrassv2.types.effective_deployment_error_type_list.serialize_json(
                value["error_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> EffectiveDeploymentStatusDetails:
    out: EffectiveDeploymentStatusDetails = {}  # type: ignore[typeddict-item]
    if "errorStack" in data:
        import aws_sdk_greengrassv2.types.effective_deployment_error_stack

        out["error_stack"] = (
            aws_sdk_greengrassv2.types.effective_deployment_error_stack.deserialize_json(
                data["errorStack"]
            )
        )
    if "errorTypes" in data:
        import aws_sdk_greengrassv2.types.effective_deployment_error_type_list

        out["error_types"] = (
            aws_sdk_greengrassv2.types.effective_deployment_error_type_list.deserialize_json(
                data["errorTypes"]
            )
        )
    return out
