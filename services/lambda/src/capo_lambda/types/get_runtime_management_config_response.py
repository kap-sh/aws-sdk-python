"""Generated from Smithy shape ``com.amazonaws.lambda#GetRuntimeManagementConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.name_spaced_function_arn
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.update_runtime_on


class GetRuntimeManagementConfigResponse(TypedDict, closed=True):
    update_runtime_on: NotRequired[
        "capo_lambda.types.update_runtime_on.UpdateRuntimeOn"
    ]
    """<p>The current runtime update mode of the function.</p>"""
    function_arn: NotRequired[
        "capo_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of your function.</p>"""
    runtime_version_arn: NotRequired[
        "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime the function is configured to use. If the runtime update mode is <b>Manual</b>, the ARN is returned, otherwise <code>null</code> is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuntimeManagementConfigResponse) -> dict:
    out: dict = {}
    if "update_runtime_on" in value:
        import capo_lambda.types.update_runtime_on

        out["UpdateRuntimeOn"] = capo_lambda.types.update_runtime_on.serialize_json(
            value["update_runtime_on"]
        )
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    return out


def deserialize_json(data: dict) -> GetRuntimeManagementConfigResponse:
    out: GetRuntimeManagementConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateRuntimeOn") is not None:
        import capo_lambda.types.update_runtime_on

        out["update_runtime_on"] = capo_lambda.types.update_runtime_on.deserialize_json(
            data["UpdateRuntimeOn"]
        )
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    if data.get("RuntimeVersionArn") is not None:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    return out
