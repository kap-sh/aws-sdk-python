"""Generated from Smithy shape ``com.amazonaws.glue#GetUserDefinedFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.user_defined_function


class GetUserDefinedFunctionResponse(TypedDict, closed=True):
    user_defined_function: NotRequired[
        "capo_glue.types.user_defined_function.UserDefinedFunction"
    ]
    """<p>The requested function definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserDefinedFunctionResponse) -> dict:
    out: dict = {}
    if "user_defined_function" in value:
        import capo_glue.types.user_defined_function

        out["UserDefinedFunction"] = (
            capo_glue.types.user_defined_function.serialize_aws_json_1_1(
                value["user_defined_function"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserDefinedFunctionResponse:
    out: GetUserDefinedFunctionResponse = {}  # type: ignore[typeddict-item]
    if "UserDefinedFunction" in data:
        import capo_glue.types.user_defined_function

        out["user_defined_function"] = (
            capo_glue.types.user_defined_function.deserialize_aws_json_1_1(
                data["UserDefinedFunction"]
            )
        )
    return out
