"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsByCodeSigningConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_arn_list
    import aws_sdk_lambda.types.string


class ListFunctionsByCodeSigningConfigResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    function_arns: NotRequired["aws_sdk_lambda.types.function_arn_list.FunctionArnList"]
    """<p>The function ARNs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsByCodeSigningConfigResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "function_arns" in value:
        import aws_sdk_lambda.types.function_arn_list

        out["FunctionArns"] = aws_sdk_lambda.types.function_arn_list.serialize_json(
            value["function_arns"]
        )
    return out


def deserialize_json(data: dict) -> ListFunctionsByCodeSigningConfigResponse:
    out: ListFunctionsByCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "FunctionArns" in data:
        import aws_sdk_lambda.types.function_arn_list

        out["function_arns"] = aws_sdk_lambda.types.function_arn_list.deserialize_json(
            data["FunctionArns"]
        )
    return out
