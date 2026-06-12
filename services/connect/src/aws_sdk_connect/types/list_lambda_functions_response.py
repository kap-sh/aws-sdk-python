"""Generated from Smithy shape ``com.amazonaws.connect#ListLambdaFunctionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.function_arns_list
    import aws_sdk_connect.types.next_token


class ListLambdaFunctionsResponse(TypedDict):
    lambda_functions: NotRequired[
        "aws_sdk_connect.types.function_arns_list.FunctionArnsList"
    ]
    """<p>The Lambdafunction ARNs associated with the specified instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLambdaFunctionsResponse) -> dict:
    out: dict = {}
    if "lambda_functions" in value:
        import aws_sdk_connect.types.function_arns_list

        out["LambdaFunctions"] = (
            aws_sdk_connect.types.function_arns_list.serialize_json(
                value["lambda_functions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLambdaFunctionsResponse:
    out: ListLambdaFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "LambdaFunctions" in data:
        import aws_sdk_connect.types.function_arns_list

        out["lambda_functions"] = (
            aws_sdk_connect.types.function_arns_list.deserialize_json(
                data["LambdaFunctions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
