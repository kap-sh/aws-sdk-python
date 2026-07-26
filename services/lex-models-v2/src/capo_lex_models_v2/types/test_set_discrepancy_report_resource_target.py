"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyReportResourceTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target


class TestSetDiscrepancyReportResourceTarget(TypedDict, closed=True):
    bot_alias_target: NotRequired[
        "capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target.TestSetDiscrepancyReportBotAliasTarget"
    ]
    """<p>Contains information about the bot alias used as the resource for the test set discrepancy report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyReportResourceTarget) -> dict:
    out: dict = {}
    if "bot_alias_target" in value:
        import capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target

        out["botAliasTarget"] = (
            capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target.serialize_json(
                value["bot_alias_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestSetDiscrepancyReportResourceTarget:
    out: TestSetDiscrepancyReportResourceTarget = {}  # type: ignore[typeddict-item]
    if "botAliasTarget" in data:
        import capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target

        out["bot_alias_target"] = (
            capo_lex_models_v2.types.test_set_discrepancy_report_bot_alias_target.deserialize_json(
                data["botAliasTarget"]
            )
        )
    return out
