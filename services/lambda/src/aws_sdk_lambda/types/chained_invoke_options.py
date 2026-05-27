"""Generated from Smithy shape ``com.amazonaws.lambda#ChainedInvokeOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.tenant_id


class ChainedInvokeOptions(TypedDict):
    function_name: (
        "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName"
    )
    """<p>The name or ARN of the Lambda function to invoke.</p>"""
    tenant_id: NotRequired["aws_sdk_lambda.types.tenant_id.TenantId"]
    """<p>The tenant identifier for the chained invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChainedInvokeOptions) -> dict:
    out: dict = {}
    out["FunctionName"] = value["function_name"]
    if "tenant_id" in value:
        out["TenantId"] = value["tenant_id"]
    return out


def deserialize_json(data: dict) -> ChainedInvokeOptions:
    out: ChainedInvokeOptions = {}  # type: ignore[typeddict-item]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError("ChainedInvokeOptions.function_name required")
    if "TenantId" in data:
        out["tenant_id"] = data["TenantId"]
    return out
