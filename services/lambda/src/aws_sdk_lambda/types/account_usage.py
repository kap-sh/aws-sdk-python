"""Generated from Smithy shape ``com.amazonaws.lambda#AccountUsage``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.long


class AccountUsage(TypedDict):
    total_code_size: "aws_sdk_lambda.types.long.Long"
    """<p>The amount of storage space, in bytes, that's being used by deployment packages and layer archives.</p>"""
    function_count: "aws_sdk_lambda.types.long.Long"
    """<p>The number of Lambda functions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountUsage) -> dict:
    out: dict = {}
    out["TotalCodeSize"] = value.get("total_code_size", 0)
    out["FunctionCount"] = value.get("function_count", 0)
    return out


def deserialize_json(data: dict) -> AccountUsage:
    out: AccountUsage = {}  # type: ignore[typeddict-item]
    if "TotalCodeSize" in data:
        out["total_code_size"] = data["TotalCodeSize"]
    else:
        out["total_code_size"] = 0
    if "FunctionCount" in data:
        out["function_count"] = data["FunctionCount"]
    else:
        out["function_count"] = 0
    return out
