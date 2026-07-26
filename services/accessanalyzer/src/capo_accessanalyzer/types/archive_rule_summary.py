"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ArchiveRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.filter_criteria_map
    import capo_accessanalyzer.types.name
    import capo_accessanalyzer.types.timestamp


class ArchiveRuleSummary(TypedDict, closed=True):
    rule_name: "capo_accessanalyzer.types.name.Name"
    """<p>The name of the archive rule.</p>"""
    filter: "capo_accessanalyzer.types.filter_criteria_map.FilterCriteriaMap"
    """<p>A filter used to define the archive rule.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the archive rule was created.</p>"""
    updated_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the archive rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveRuleSummary) -> dict:
    out: dict = {}
    out["ruleName"] = value["rule_name"]
    import capo_accessanalyzer.types.filter_criteria_map

    out["filter"] = capo_accessanalyzer.types.filter_criteria_map.serialize_json(
        value["filter"]
    )
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_accessanalyzer.types.timestamp

    out["updatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ArchiveRuleSummary:
    out: ArchiveRuleSummary = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("ArchiveRuleSummary.rule_name required")
    if "filter" in data:
        import capo_accessanalyzer.types.filter_criteria_map

        out["filter"] = capo_accessanalyzer.types.filter_criteria_map.deserialize_json(
            data["filter"]
        )
    else:
        raise DeserializationError("ArchiveRuleSummary.filter required")
    if "createdAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ArchiveRuleSummary.created_at required")
    if "updatedAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["updated_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ArchiveRuleSummary.updated_at required")
    return out
