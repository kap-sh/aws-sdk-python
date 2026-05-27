"""Generated from Smithy shape ``com.amazonaws.lambda#ListVersionsByFunctionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.function_list
    import aws_sdk_lambda.types.string


class ListVersionsByFunctionResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    versions: NotRequired["aws_sdk_lambda.types.function_list.FunctionList"]
    """<p>A list of Lambda function versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsByFunctionResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "versions" in value:
        import aws_sdk_lambda.types.function_list

        out["Versions"] = aws_sdk_lambda.types.function_list.serialize_json(
            value["versions"]
        )
    return out


def deserialize_json(data: dict) -> ListVersionsByFunctionResponse:
    out: ListVersionsByFunctionResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Versions" in data:
        import aws_sdk_lambda.types.function_list

        out["versions"] = aws_sdk_lambda.types.function_list.deserialize_json(
            data["Versions"]
        )
    return out
