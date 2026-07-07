"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionRecursionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.unqualified_function_name


class GetFunctionRecursionConfigRequest(TypedDict, closed=True):
    function_name: (
        "aws_sdk_lambda.types.unqualified_function_name.UnqualifiedFunctionName"
    )
    """<p>The name of the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionRecursionConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionRecursionConfigRequest:
    out: GetFunctionRecursionConfigRequest = {}  # type: ignore[typeddict-item]
    return out
