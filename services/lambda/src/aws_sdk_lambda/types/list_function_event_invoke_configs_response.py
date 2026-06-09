"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionEventInvokeConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_event_invoke_config_list
    import aws_sdk_lambda.types.string


class ListFunctionEventInvokeConfigsResponse(TypedDict):
    function_event_invoke_configs: NotRequired[
        "aws_sdk_lambda.types.function_event_invoke_config_list.FunctionEventInvokeConfigList"
    ]
    """<p>A list of configurations.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionEventInvokeConfigsResponse) -> dict:
    out: dict = {}
    if "function_event_invoke_configs" in value:
        import aws_sdk_lambda.types.function_event_invoke_config_list

        out["FunctionEventInvokeConfigs"] = (
            aws_sdk_lambda.types.function_event_invoke_config_list.serialize_json(
                value["function_event_invoke_configs"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionEventInvokeConfigsResponse:
    out: ListFunctionEventInvokeConfigsResponse = {}  # type: ignore[typeddict-item]
    if "FunctionEventInvokeConfigs" in data:
        import aws_sdk_lambda.types.function_event_invoke_config_list

        out["function_event_invoke_configs"] = (
            aws_sdk_lambda.types.function_event_invoke_config_list.deserialize_json(
                data["FunctionEventInvokeConfigs"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
