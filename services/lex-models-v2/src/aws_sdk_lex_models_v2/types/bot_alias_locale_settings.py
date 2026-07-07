"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasLocaleSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boolean
    import aws_sdk_lex_models_v2.types.code_hook_specification


class BotAliasLocaleSettings(TypedDict, closed=True):
    enabled: "aws_sdk_lex_models_v2.types.boolean.Boolean"
    """<p>Determines whether the locale is enabled for the bot. If the value is <code>false</code>, the locale isn't available for use.</p>"""
    code_hook_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.code_hook_specification.CodeHookSpecification"
    ]
    """<p>Specifies the Lambda function that should be used in the locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasLocaleSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "code_hook_specification" in value:
        import aws_sdk_lex_models_v2.types.code_hook_specification

        out["codeHookSpecification"] = (
            aws_sdk_lex_models_v2.types.code_hook_specification.serialize_json(
                value["code_hook_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotAliasLocaleSettings:
    out: BotAliasLocaleSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "codeHookSpecification" in data:
        import aws_sdk_lex_models_v2.types.code_hook_specification

        out["code_hook_specification"] = (
            aws_sdk_lex_models_v2.types.code_hook_specification.deserialize_json(
                data["codeHookSpecification"]
            )
        )
    return out
