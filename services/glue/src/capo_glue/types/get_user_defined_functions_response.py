"""Generated from Smithy shape ``com.amazonaws.glue#GetUserDefinedFunctionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.token
    import capo_glue.types.user_defined_function_list


class GetUserDefinedFunctionsResponse(TypedDict, closed=True):
    user_defined_functions: NotRequired[
        "capo_glue.types.user_defined_function_list.UserDefinedFunctionList"
    ]
    """<p>A list of requested function definitions.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if the list of functions returned does not include the last requested function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserDefinedFunctionsResponse) -> dict:
    out: dict = {}
    if "user_defined_functions" in value:
        import capo_glue.types.user_defined_function_list

        out["UserDefinedFunctions"] = (
            capo_glue.types.user_defined_function_list.serialize_aws_json_1_1(
                value["user_defined_functions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserDefinedFunctionsResponse:
    out: GetUserDefinedFunctionsResponse = {}  # type: ignore[typeddict-item]
    if "UserDefinedFunctions" in data:
        import capo_glue.types.user_defined_function_list

        out["user_defined_functions"] = (
            capo_glue.types.user_defined_function_list.deserialize_aws_json_1_1(
                data["UserDefinedFunctions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
