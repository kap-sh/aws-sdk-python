"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetArchiveRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.archive_rule_summary


class GetArchiveRuleResponse(TypedDict, closed=True):
    archive_rule: "capo_accessanalyzer.types.archive_rule_summary.ArchiveRuleSummary"


# --- restJson1 ser/de ---
def serialize_json(value: GetArchiveRuleResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.archive_rule_summary

    out["archiveRule"] = capo_accessanalyzer.types.archive_rule_summary.serialize_json(
        value["archive_rule"]
    )
    return out


def deserialize_json(data: dict) -> GetArchiveRuleResponse:
    out: GetArchiveRuleResponse = {}  # type: ignore[typeddict-item]
    if "archiveRule" in data:
        import capo_accessanalyzer.types.archive_rule_summary

        out["archive_rule"] = (
            capo_accessanalyzer.types.archive_rule_summary.deserialize_json(
                data["archiveRule"]
            )
        )
    else:
        raise DeserializationError("GetArchiveRuleResponse.archive_rule required")
    return out
