"""Generated from Smithy shape ``com.amazonaws.lambda#GetRuntimeManagementConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.name_spaced_function_arn
    import aws_sdk_lambda.types.runtime_version_arn
    import aws_sdk_lambda.types.update_runtime_on


class GetRuntimeManagementConfigResponse(TypedDict):
    update_runtime_on: NotRequired[
        "aws_sdk_lambda.types.update_runtime_on.UpdateRuntimeOn"
    ]
    """<p>The current runtime update mode of the function.</p>"""
    runtime_version_arn: NotRequired[
        "aws_sdk_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime the function is configured to use. If the runtime update mode is <b>Manual</b>, the ARN is returned, otherwise <code>null</code> is returned.</p>"""
    function_arn: NotRequired[
        "aws_sdk_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of your function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeManagementConfigResponse) -> dict:
    out: dict = {}
    if "update_runtime_on" in value:
        import aws_sdk_lambda.types.update_runtime_on

        out["UpdateRuntimeOn"] = aws_sdk_lambda.types.update_runtime_on.serialize_json(
            value["update_runtime_on"]
        )
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> GetRuntimeManagementConfigResponse:
    out: GetRuntimeManagementConfigResponse = {}  # type: ignore[typeddict-item]
    if "UpdateRuntimeOn" in data:
        import aws_sdk_lambda.types.update_runtime_on

        out["update_runtime_on"] = (
            aws_sdk_lambda.types.update_runtime_on.deserialize_json(
                data["UpdateRuntimeOn"]
            )
        )
    if "RuntimeVersionArn" in data:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    return out
