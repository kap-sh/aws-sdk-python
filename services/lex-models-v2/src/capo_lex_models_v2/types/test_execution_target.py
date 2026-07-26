"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_test_execution_target


class TestExecutionTarget(TypedDict, closed=True):
    bot_alias_target: NotRequired[
        "capo_lex_models_v2.types.bot_alias_test_execution_target.BotAliasTestExecutionTarget"
    ]
    """<p>Contains information about the bot alias used for the test execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionTarget) -> dict:
    out: dict = {}
    if "bot_alias_target" in value:
        import capo_lex_models_v2.types.bot_alias_test_execution_target

        out["botAliasTarget"] = (
            capo_lex_models_v2.types.bot_alias_test_execution_target.serialize_json(
                value["bot_alias_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionTarget:
    out: TestExecutionTarget = {}  # type: ignore[typeddict-item]
    if "botAliasTarget" in data:
        import capo_lex_models_v2.types.bot_alias_test_execution_target

        out["bot_alias_target"] = (
            capo_lex_models_v2.types.bot_alias_test_execution_target.deserialize_json(
                data["botAliasTarget"]
            )
        )
    return out
