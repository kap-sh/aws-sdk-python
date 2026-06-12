"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetVariablesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.variable_list


class GetVariablesResult(TypedDict):
    variables: NotRequired["aws_sdk_frauddetector.types.variable_list.VariableList"]
    """<p>The names of the variables returned. </p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVariablesResult) -> dict:
    out: dict = {}
    if "variables" in value:
        import aws_sdk_frauddetector.types.variable_list

        out["variables"] = (
            aws_sdk_frauddetector.types.variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVariablesResult:
    out: GetVariablesResult = {}  # type: ignore[typeddict-item]
    if "variables" in data:
        import aws_sdk_frauddetector.types.variable_list

        out["variables"] = (
            aws_sdk_frauddetector.types.variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
