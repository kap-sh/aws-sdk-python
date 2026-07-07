"""Generated from Smithy shape ``com.amazonaws.lambda#RuntimeVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.runtime_version_arn
    import aws_sdk_lambda.types.runtime_version_error


class RuntimeVersionConfig(TypedDict, closed=True):
    runtime_version_arn: NotRequired[
        "aws_sdk_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime version you want the function to use.</p>"""
    error: NotRequired["aws_sdk_lambda.types.runtime_version_error.RuntimeVersionError"]
    """<p>Error response when Lambda is unable to retrieve the runtime version for a function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionConfig) -> dict:
    out: dict = {}
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    if "error" in value:
        import aws_sdk_lambda.types.runtime_version_error

        out["Error"] = aws_sdk_lambda.types.runtime_version_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RuntimeVersionConfig:
    out: RuntimeVersionConfig = {}  # type: ignore[typeddict-item]
    if "RuntimeVersionArn" in data:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    if "Error" in data:
        import aws_sdk_lambda.types.runtime_version_error

        out["error"] = aws_sdk_lambda.types.runtime_version_error.deserialize_json(
            data["Error"]
        )
    return out
