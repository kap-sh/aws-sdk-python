"""Generated from Smithy shape ``com.amazonaws.lambda#AccountLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.integer
    import aws_sdk_lambda.types.long
    import aws_sdk_lambda.types.unreserved_concurrent_executions


class AccountLimit(TypedDict, closed=True):
    total_code_size: "aws_sdk_lambda.types.long.Long"
    """<p>The amount of storage space that you can use for all deployment packages and layer archives.</p>"""
    code_size_unzipped: "aws_sdk_lambda.types.long.Long"
    """<p>The maximum size of a function's deployment package and layers when they're extracted.</p>"""
    code_size_zipped: "aws_sdk_lambda.types.long.Long"
    """<p>The maximum size of a deployment package when it's uploaded directly to Lambda. Use Amazon S3 for larger files.</p>"""
    concurrent_executions: "aws_sdk_lambda.types.integer.Integer"
    """<p>The maximum number of simultaneous function executions.</p>"""
    unreserved_concurrent_executions: NotRequired[
        "aws_sdk_lambda.types.unreserved_concurrent_executions.UnreservedConcurrentExecutions"
    ]
    """<p>The maximum number of simultaneous function executions, minus the capacity that's reserved for individual functions with <a>PutFunctionConcurrency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountLimit) -> dict:
    out: dict = {}
    out["TotalCodeSize"] = value.get("total_code_size", 0)
    out["CodeSizeUnzipped"] = value.get("code_size_unzipped", 0)
    out["CodeSizeZipped"] = value.get("code_size_zipped", 0)
    out["ConcurrentExecutions"] = value.get("concurrent_executions", 0)
    if "unreserved_concurrent_executions" in value:
        out["UnreservedConcurrentExecutions"] = value[
            "unreserved_concurrent_executions"
        ]
    return out


def deserialize_json(data: dict) -> AccountLimit:
    out: AccountLimit = {}  # type: ignore[typeddict-item]
    if "TotalCodeSize" in data:
        out["total_code_size"] = data["TotalCodeSize"]
    else:
        out["total_code_size"] = 0
    if "CodeSizeUnzipped" in data:
        out["code_size_unzipped"] = data["CodeSizeUnzipped"]
    else:
        out["code_size_unzipped"] = 0
    if "CodeSizeZipped" in data:
        out["code_size_zipped"] = data["CodeSizeZipped"]
    else:
        out["code_size_zipped"] = 0
    if "ConcurrentExecutions" in data:
        out["concurrent_executions"] = data["ConcurrentExecutions"]
    else:
        out["concurrent_executions"] = 0
    if "UnreservedConcurrentExecutions" in data:
        out["unreserved_concurrent_executions"] = data["UnreservedConcurrentExecutions"]
    return out
