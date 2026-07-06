"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionRecursionConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.recursive_loop


class PutFunctionRecursionConfigResponse(TypedDict, closed=True):
    recursive_loop: NotRequired["aws_sdk_lambda.types.recursive_loop.RecursiveLoop"]
    """<p>The status of your function's recursive loop detection configuration.</p> <p>When this value is set to <code>Allow</code>and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.</p> <p>When this value is set to <code>Terminate</code> and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionRecursionConfigResponse) -> dict:
    out: dict = {}
    if "recursive_loop" in value:
        import aws_sdk_lambda.types.recursive_loop

        out["RecursiveLoop"] = aws_sdk_lambda.types.recursive_loop.serialize_json(
            value["recursive_loop"]
        )
    return out


def deserialize_json(data: dict) -> PutFunctionRecursionConfigResponse:
    out: PutFunctionRecursionConfigResponse = {}  # type: ignore[typeddict-item]
    if "RecursiveLoop" in data:
        import aws_sdk_lambda.types.recursive_loop

        out["recursive_loop"] = aws_sdk_lambda.types.recursive_loop.deserialize_json(
            data["RecursiveLoop"]
        )
    return out
