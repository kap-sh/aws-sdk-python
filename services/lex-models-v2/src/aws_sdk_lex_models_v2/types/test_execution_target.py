"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_test_execution_target


class TestExecutionTarget(TypedDict):
    bot_alias_target: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_test_execution_target.BotAliasTestExecutionTarget"
    ]
    """<p>Contains information about the bot alias used for the test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionTarget) -> dict:
    out: dict = {}
    if "bot_alias_target" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_test_execution_target

        out["botAliasTarget"] = (
            aws_sdk_lex_models_v2.types.bot_alias_test_execution_target.serialize_json(
                value["bot_alias_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionTarget:
    out: TestExecutionTarget = {}  # type: ignore[typeddict-item]
    if "botAliasTarget" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_test_execution_target

        out["bot_alias_target"] = (
            aws_sdk_lex_models_v2.types.bot_alias_test_execution_target.deserialize_json(
                data["botAliasTarget"]
            )
        )
    return out
