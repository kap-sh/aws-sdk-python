"""Generated from Smithy shape ``com.amazonaws.lambda#PutFunctionScalingConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.state


class PutFunctionScalingConfigResponse(TypedDict, closed=True):
    function_state: NotRequired["capo_lambda.types.state.State"]
    """<p>The current state of the function after applying the scaling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionScalingConfigResponse) -> dict:
    out: dict = {}
    if "function_state" in value:
        import capo_lambda.types.state

        out["FunctionState"] = capo_lambda.types.state.serialize_json(
            value["function_state"]
        )
    return out


def deserialize_json(data: dict) -> PutFunctionScalingConfigResponse:
    out: PutFunctionScalingConfigResponse = {}  # type: ignore[typeddict-item]
    if "FunctionState" in data:
        import capo_lambda.types.state

        out["function_state"] = capo_lambda.types.state.deserialize_json(
            data["FunctionState"]
        )
    return out
