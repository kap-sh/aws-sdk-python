"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleCondition``."""

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError


class RuleCondition(TypedDict, closed=True):
    rule_name: "str"
    """<p>A name for the matching rule.</p> <p>For example: <code>Rule1</code> </p>"""
    condition: "str"
    """<p>A statement that specifies the conditions for a matching rule.</p> <p>If your data is accurate, use an Exact matching function: <code>Exact</code> or <code>ExactManyToMany</code>. </p> <p>If your data has variations in spelling or pronunciation, use a Fuzzy matching function: <code>Cosine</code>, <code>Levenshtein</code>, or <code>Soundex</code>. </p> <p>Use operators if you want to combine (<code>AND</code>), separate (<code>OR</code>), or group matching functions <code>(...)</code>.</p> <p>For example: <code>(Cosine(a, 10) AND Exact(b, true)) OR ExactManyToMany(c, d)</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleCondition) -> dict:
    out: dict = {}
    out["ruleName"] = value["rule_name"]
    out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> RuleCondition:
    out: RuleCondition = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("RuleCondition.rule_name required")
    if "condition" in data:
        out["condition"] = data["condition"]
    else:
        raise DeserializationError("RuleCondition.condition required")
    return out
