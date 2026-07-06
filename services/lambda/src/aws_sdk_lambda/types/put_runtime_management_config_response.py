"""Generated from Smithy shape ``com.amazonaws.lambda#PutRuntimeManagementConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.runtime_version_arn
    import aws_sdk_lambda.types.update_runtime_on


class PutRuntimeManagementConfigResponse(TypedDict, closed=True):
    update_runtime_on: "aws_sdk_lambda.types.update_runtime_on.UpdateRuntimeOn"
    """<p>The runtime update mode.</p>"""
    function_arn: "aws_sdk_lambda.types.function_arn.FunctionArn"
    """<p>The ARN of the function</p>"""
    runtime_version_arn: NotRequired[
        "aws_sdk_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime the function is configured to use. If the runtime update mode is <b>manual</b>, the ARN is returned, otherwise <code>null</code> is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRuntimeManagementConfigResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.update_runtime_on

    out["UpdateRuntimeOn"] = aws_sdk_lambda.types.update_runtime_on.serialize_json(
        value["update_runtime_on"]
    )
    out["FunctionArn"] = value["function_arn"]
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    return out


def deserialize_json(data: dict) -> PutRuntimeManagementConfigResponse:
    out: PutRuntimeManagementConfigResponse = {}  # type: ignore[typeddict-item]
    if "UpdateRuntimeOn" in data:
        import aws_sdk_lambda.types.update_runtime_on

        out["update_runtime_on"] = (
            aws_sdk_lambda.types.update_runtime_on.deserialize_json(
                data["UpdateRuntimeOn"]
            )
        )
    else:
        raise DeserializationError(
            "PutRuntimeManagementConfigResponse.update_runtime_on required"
        )
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError(
            "PutRuntimeManagementConfigResponse.function_arn required"
        )
    if "RuntimeVersionArn" in data:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    return out
