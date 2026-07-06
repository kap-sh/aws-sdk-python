"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionScalingConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.state


class PutFunctionScalingConfigResponse(TypedDict, closed=True):
    function_state: NotRequired["aws_sdk_lambda.types.state.State"]
    """<p>The current state of the function after applying the scaling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionScalingConfigResponse) -> dict:
    out: dict = {}
    if "function_state" in value:
        import aws_sdk_lambda.types.state

        out["FunctionState"] = aws_sdk_lambda.types.state.serialize_json(
            value["function_state"]
        )
    return out


def deserialize_json(data: dict) -> PutFunctionScalingConfigResponse:
    out: PutFunctionScalingConfigResponse = {}  # type: ignore[typeddict-item]
    if "FunctionState" in data:
        import aws_sdk_lambda.types.state

        out["function_state"] = aws_sdk_lambda.types.state.deserialize_json(
            data["FunctionState"]
        )
    return out
