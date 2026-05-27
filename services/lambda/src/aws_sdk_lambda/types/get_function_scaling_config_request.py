"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionScalingConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.published_function_qualifier
    import aws_sdk_lambda.types.unqualified_function_name


class GetFunctionScalingConfigRequest(TypedDict):
    function_name: (
        "aws_sdk_lambda.types.unqualified_function_name.UnqualifiedFunctionName"
    )
    """<p>The name or ARN of the Lambda function.</p>"""
    qualifier: (
        "aws_sdk_lambda.types.published_function_qualifier.PublishedFunctionQualifier"
    )
    """<p>Specify a version or alias to get the scaling configuration for a published version of the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionScalingConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionScalingConfigRequest:
    out: GetFunctionScalingConfigRequest = {}  # type: ignore[typeddict-item]
    return out
