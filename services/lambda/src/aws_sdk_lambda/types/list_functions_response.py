"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_list
    import aws_sdk_lambda.types.string


class ListFunctionsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    functions: NotRequired["aws_sdk_lambda.types.function_list.FunctionList"]
    """<p>A list of Lambda functions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "functions" in value:
        import aws_sdk_lambda.types.function_list

        out["Functions"] = aws_sdk_lambda.types.function_list.serialize_json(
            value["functions"]
        )
    return out


def deserialize_json(data: dict) -> ListFunctionsResponse:
    out: ListFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Functions" in data:
        import aws_sdk_lambda.types.function_list

        out["functions"] = aws_sdk_lambda.types.function_list.deserialize_json(
            data["Functions"]
        )
    return out
