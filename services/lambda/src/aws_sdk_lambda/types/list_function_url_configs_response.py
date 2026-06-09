"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionUrlConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_url_config_list
    import aws_sdk_lambda.types.string


class ListFunctionUrlConfigsResponse(TypedDict):
    function_url_configs: (
        "aws_sdk_lambda.types.function_url_config_list.FunctionUrlConfigList"
    )
    """<p>A list of function URL configurations.</p>"""
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionUrlConfigsResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.function_url_config_list

    out["FunctionUrlConfigs"] = (
        aws_sdk_lambda.types.function_url_config_list.serialize_json(
            value["function_url_configs"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionUrlConfigsResponse:
    out: ListFunctionUrlConfigsResponse = {}  # type: ignore[typeddict-item]
    if "FunctionUrlConfigs" in data:
        import aws_sdk_lambda.types.function_url_config_list

        out["function_url_configs"] = (
            aws_sdk_lambda.types.function_url_config_list.deserialize_json(
                data["FunctionUrlConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "ListFunctionUrlConfigsResponse.function_url_configs required"
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
