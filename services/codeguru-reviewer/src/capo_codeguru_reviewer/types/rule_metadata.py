"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RuleMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.long_description
    import capo_codeguru_reviewer.types.rule_id
    import capo_codeguru_reviewer.types.rule_name
    import capo_codeguru_reviewer.types.rule_tags
    import capo_codeguru_reviewer.types.short_description


class RuleMetadata(TypedDict, closed=True):
    rule_id: NotRequired["capo_codeguru_reviewer.types.rule_id.RuleId"]
    """<p>The ID of the rule.</p>"""
    rule_name: NotRequired["capo_codeguru_reviewer.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    short_description: NotRequired[
        "capo_codeguru_reviewer.types.short_description.ShortDescription"
    ]
    """<p>A short description of the rule.</p>"""
    long_description: NotRequired[
        "capo_codeguru_reviewer.types.long_description.LongDescription"
    ]
    """<p>A long description of the rule.</p>"""
    rule_tags: NotRequired["capo_codeguru_reviewer.types.rule_tags.RuleTags"]
    """<p>Tags that are associated with the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleMetadata) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "short_description" in value:
        out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "rule_tags" in value:
        import capo_codeguru_reviewer.types.rule_tags

        out["RuleTags"] = capo_codeguru_reviewer.types.rule_tags.serialize_json(
            value["rule_tags"]
        )
    return out


def deserialize_json(data: dict) -> RuleMetadata:
    out: RuleMetadata = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "ShortDescription" in data:
        out["short_description"] = data["ShortDescription"]
    if "LongDescription" in data:
        out["long_description"] = data["LongDescription"]
    if "RuleTags" in data:
        import capo_codeguru_reviewer.types.rule_tags

        out["rule_tags"] = capo_codeguru_reviewer.types.rule_tags.deserialize_json(
            data["RuleTags"]
        )
    return out
