"""Generated from Smithy shape ``com.amazonaws.cognitosync#Events``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.cognito_event_type
    import capo_cognito_sync.types.lambda_function_arn

Events: TypeAlias = dict[
    "capo_cognito_sync.types.cognito_event_type.CognitoEventType",
    "capo_cognito_sync.types.lambda_function_arn.LambdaFunctionArn",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Events) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Events:
    out: Events = {}
    for key, value in data.items():
        out[key] = value
    return out
