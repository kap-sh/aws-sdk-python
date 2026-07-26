"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionRecursionConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.recursive_loop


class GetFunctionRecursionConfigResponse(TypedDict, closed=True):
    recursive_loop: NotRequired["capo_lambda.types.recursive_loop.RecursiveLoop"]
    """<p>If your function's recursive loop detection configuration is <code>Allow</code>, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop.</p> <p>If your function's recursive loop detection configuration is <code>Terminate</code>, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.</p> <p>By default, Lambda sets your function's configuration to <code>Terminate</code>. You can update this configuration using the <a>PutFunctionRecursionConfig</a> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionRecursionConfigResponse) -> dict:
    out: dict = {}
    if "recursive_loop" in value:
        import capo_lambda.types.recursive_loop

        out["RecursiveLoop"] = capo_lambda.types.recursive_loop.serialize_json(
            value["recursive_loop"]
        )
    return out


def deserialize_json(data: dict) -> GetFunctionRecursionConfigResponse:
    out: GetFunctionRecursionConfigResponse = {}  # type: ignore[typeddict-item]
    if "RecursiveLoop" in data:
        import capo_lambda.types.recursive_loop

        out["recursive_loop"] = capo_lambda.types.recursive_loop.deserialize_json(
            data["RecursiveLoop"]
        )
    return out
