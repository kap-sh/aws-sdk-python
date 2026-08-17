"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionEventInvokeConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_event_invoke_config_list
    import capo_lambda.types.string


class ListFunctionEventInvokeConfigsResponse(TypedDict, closed=True):
    function_event_invoke_configs: NotRequired[
        "capo_lambda.types.function_event_invoke_config_list.FunctionEventInvokeConfigList"
    ]
    """<p>A list of configurations.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionEventInvokeConfigsResponse) -> dict:
    out: dict = {}
    if "function_event_invoke_configs" in value:
        import capo_lambda.types.function_event_invoke_config_list

        out["FunctionEventInvokeConfigs"] = (
            capo_lambda.types.function_event_invoke_config_list.serialize_json(
                value["function_event_invoke_configs"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionEventInvokeConfigsResponse:
    out: ListFunctionEventInvokeConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FunctionEventInvokeConfigs") is not None:
        import capo_lambda.types.function_event_invoke_config_list

        out["function_event_invoke_configs"] = (
            capo_lambda.types.function_event_invoke_config_list.deserialize_json(
                data["FunctionEventInvokeConfigs"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
