"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PromptAttemptsSpecificationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.prompt_attempt
    import aws_sdk_lex_models_v2.types.prompt_attempt_specification

PromptAttemptsSpecificationMap: TypeAlias = dict[
    "aws_sdk_lex_models_v2.types.prompt_attempt.PromptAttempt",
    "aws_sdk_lex_models_v2.types.prompt_attempt_specification.PromptAttemptSpecification",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PromptAttemptsSpecificationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lex_models_v2.types.prompt_attempt
        import aws_sdk_lex_models_v2.types.prompt_attempt_specification

        out[aws_sdk_lex_models_v2.types.prompt_attempt.serialize_json(key)] = (
            aws_sdk_lex_models_v2.types.prompt_attempt_specification.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> PromptAttemptsSpecificationMap:
    out: PromptAttemptsSpecificationMap = {}
    for key, value in data.items():
        import aws_sdk_lex_models_v2.types.prompt_attempt
        import aws_sdk_lex_models_v2.types.prompt_attempt_specification

        out[aws_sdk_lex_models_v2.types.prompt_attempt.deserialize_json(key)] = (
            aws_sdk_lex_models_v2.types.prompt_attempt_specification.deserialize_json(
                value
            )
        )
    return out
