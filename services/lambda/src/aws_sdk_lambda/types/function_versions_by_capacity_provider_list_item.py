"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionsByCapacityProviderListItem``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.name_spaced_function_arn
    import aws_sdk_lambda.types.state


class FunctionVersionsByCapacityProviderListItem(TypedDict):
    function_arn: "aws_sdk_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the function version.</p>"""
    state: "aws_sdk_lambda.types.state.State"
    """<p>The current state of the function version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionVersionsByCapacityProviderListItem) -> dict:
    out: dict = {}
    out["FunctionArn"] = value["function_arn"]
    import aws_sdk_lambda.types.state

    out["State"] = aws_sdk_lambda.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> FunctionVersionsByCapacityProviderListItem:
    out: FunctionVersionsByCapacityProviderListItem = {}  # type: ignore[typeddict-item]
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    else:
        raise DeserializationError(
            "FunctionVersionsByCapacityProviderListItem.function_arn required"
        )
    if "State" in data:
        import aws_sdk_lambda.types.state

        out["state"] = aws_sdk_lambda.types.state.deserialize_json(data["State"])
    else:
        raise DeserializationError(
            "FunctionVersionsByCapacityProviderListItem.state required"
        )
    return out
