"""Generated from Smithy shape ``com.amazonaws.appsync#EvaluateCodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.app_sync_runtime
    import aws_sdk_appsync.types.code
    import aws_sdk_appsync.types.context
    import aws_sdk_appsync.types.string


class EvaluateCodeRequest(TypedDict):
    runtime: "aws_sdk_appsync.types.app_sync_runtime.AppSyncRuntime"
    """<p>The runtime to be used when evaluating the code. Currently, only the <code>APPSYNC_JS</code> runtime is supported.</p>"""
    code: "aws_sdk_appsync.types.code.Code"
    """<p>The code definition to be evaluated. Note that <code>code</code> and <code>runtime</code> are both required for this action. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>"""
    context: "aws_sdk_appsync.types.context.Context"
    """<p>The map that holds all of the contextual information for your resolver invocation. A <code>context</code> is required for this action.</p>"""
    function: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The function within the code to be evaluated. If provided, the valid values are <code>request</code> and <code>response</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateCodeRequest) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.app_sync_runtime

    out["runtime"] = aws_sdk_appsync.types.app_sync_runtime.serialize_json(
        value["runtime"]
    )
    out["code"] = value["code"]
    out["context"] = value["context"]
    if "function" in value:
        out["function"] = value["function"]
    return out


def deserialize_json(data: dict) -> EvaluateCodeRequest:
    out: EvaluateCodeRequest = {}  # type: ignore[typeddict-item]
    if "runtime" in data:
        import aws_sdk_appsync.types.app_sync_runtime

        out["runtime"] = aws_sdk_appsync.types.app_sync_runtime.deserialize_json(
            data["runtime"]
        )
    else:
        raise DeserializationError("EvaluateCodeRequest.runtime required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("EvaluateCodeRequest.code required")
    if "context" in data:
        out["context"] = data["context"]
    else:
        raise DeserializationError("EvaluateCodeRequest.context required")
    if "function" in data:
        out["function"] = data["function"]
    return out
