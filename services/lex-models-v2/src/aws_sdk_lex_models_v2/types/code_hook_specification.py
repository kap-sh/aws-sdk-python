"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CodeHookSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.lambda_code_hook


class CodeHookSpecification(TypedDict, closed=True):
    lambda_code_hook: "aws_sdk_lex_models_v2.types.lambda_code_hook.LambdaCodeHook"


# --- restJson1 ser/de ---
def serialize_json(value: CodeHookSpecification) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.lambda_code_hook

    out["lambdaCodeHook"] = aws_sdk_lex_models_v2.types.lambda_code_hook.serialize_json(
        value["lambda_code_hook"]
    )
    return out


def deserialize_json(data: dict) -> CodeHookSpecification:
    out: CodeHookSpecification = {}  # type: ignore[typeddict-item]
    if "lambdaCodeHook" in data:
        import aws_sdk_lex_models_v2.types.lambda_code_hook

        out["lambda_code_hook"] = (
            aws_sdk_lex_models_v2.types.lambda_code_hook.deserialize_json(
                data["lambdaCodeHook"]
            )
        )
    else:
        raise DeserializationError("CodeHookSpecification.lambda_code_hook required")
    return out
