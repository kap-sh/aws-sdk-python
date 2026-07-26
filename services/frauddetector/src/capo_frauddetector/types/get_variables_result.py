"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetVariablesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string
    import capo_frauddetector.types.variable_list


class GetVariablesResult(TypedDict, closed=True):
    variables: NotRequired["capo_frauddetector.types.variable_list.VariableList"]
    """<p>The names of the variables returned. </p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token to be used in subsequent requests. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVariablesResult) -> dict:
    out: dict = {}
    if "variables" in value:
        import capo_frauddetector.types.variable_list

        out["variables"] = (
            capo_frauddetector.types.variable_list.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVariablesResult:
    out: GetVariablesResult = {}  # type: ignore[typeddict-item]
    if "variables" in data:
        import capo_frauddetector.types.variable_list

        out["variables"] = (
            capo_frauddetector.types.variable_list.deserialize_aws_json_1_1(
                data["variables"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
