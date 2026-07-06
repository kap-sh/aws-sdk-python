"""Generated from Smithy shape ``com.amazonaws.mediatailor#FunctionRef``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class FunctionRef(TypedDict, closed=True):
    run_condition: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>An optional expression that evaluates to a boolean. MediaTailor evaluates this expression immediately before running the step, using the accumulated state at that point in the sequence. If the expression evaluates to <code>false</code>, MediaTailor skips the step and moves to the next one. If omitted, the step always runs.</p>"""
    function_id: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The identifier of the child function to execute in this step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRef) -> dict:
    out: dict = {}
    if "run_condition" in value:
        out["RunCondition"] = value["run_condition"]
    if "function_id" in value:
        out["FunctionId"] = value["function_id"]
    return out


def deserialize_json(data: dict) -> FunctionRef:
    out: FunctionRef = {}  # type: ignore[typeddict-item]
    if "RunCondition" in data:
        out["run_condition"] = data["RunCondition"]
    if "FunctionId" in data:
        out["function_id"] = data["FunctionId"]
    return out
