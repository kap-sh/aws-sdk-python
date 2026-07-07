"""Generated from Smithy shape ``com.amazonaws.guardduty#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.eq
    import aws_sdk_guardduty.types.equals
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.long
    import aws_sdk_guardduty.types.matches
    import aws_sdk_guardduty.types.neq
    import aws_sdk_guardduty.types.not_equals
    import aws_sdk_guardduty.types.not_matches


class Condition(TypedDict, closed=True):
    eq: NotRequired["aws_sdk_guardduty.types.eq.Eq"]
    """<p>Represents the <i>equal</i> condition to be applied to a single field when querying for findings.</p> <p>Max values: 50</p>"""
    neq: NotRequired["aws_sdk_guardduty.types.neq.Neq"]
    """<p>Represents the <i>not equal</i> condition to be applied to a single field when querying for findings.</p> <p>Max values: 50</p>"""
    gt: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Represents a <i>greater than</i> condition to be applied to a single field when querying for findings.</p>"""
    gte: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Represents a <i>greater than or equal</i> condition to be applied to a single field when querying for findings.</p>"""
    lt: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Represents a <i>less than</i> condition to be applied to a single field when querying for findings.</p>"""
    lte: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Represents a <i>less than or equal</i> condition to be applied to a single field when querying for findings.</p>"""
    equals: NotRequired["aws_sdk_guardduty.types.equals.Equals"]
    """<p>Represents an <i>equal</i> <b/> condition to be applied to a single field when querying for findings.</p> <p>Max values: 50</p>"""
    not_equals: NotRequired["aws_sdk_guardduty.types.not_equals.NotEquals"]
    """<p>Represents a <i>not equal</i> <b/> condition to be applied to a single field when querying for findings.</p> <p>Max values: 50</p>"""
    greater_than: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents a <i>greater than</i> condition to be applied to a single field when querying for findings.</p>"""
    greater_than_or_equal: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents a <i>greater than or equal</i> condition to be applied to a single field when querying for findings.</p>"""
    less_than: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents a <i>less than</i> condition to be applied to a single field when querying for findings.</p>"""
    less_than_or_equal: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents a <i>less than or equal</i> condition to be applied to a single field when querying for findings.</p>"""
    matches: NotRequired["aws_sdk_guardduty.types.matches.Matches"]
    """<p>Represents the <i>match</i> condition to be applied to a single field when querying for findings. </p> <note> <p> The <i>matches</i> condition is available only for create-filter and update-filter APIs. </p> </note>"""
    not_matches: NotRequired["aws_sdk_guardduty.types.not_matches.NotMatches"]
    """<p>Represents the <i>not match</i> condition to be applied to a single field when querying for findings. </p> <note> <p> The <i>not-matches</i> condition is available only for create-filter and update-filter APIs. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "eq" in value:
        import aws_sdk_guardduty.types.eq

        out["eq"] = aws_sdk_guardduty.types.eq.serialize_json(value["eq"])
    if "neq" in value:
        import aws_sdk_guardduty.types.neq

        out["neq"] = aws_sdk_guardduty.types.neq.serialize_json(value["neq"])
    if "gt" in value:
        out["gt"] = value["gt"]
    if "gte" in value:
        out["gte"] = value["gte"]
    if "lt" in value:
        out["lt"] = value["lt"]
    if "lte" in value:
        out["lte"] = value["lte"]
    if "equals" in value:
        import aws_sdk_guardduty.types.equals

        out["equals"] = aws_sdk_guardduty.types.equals.serialize_json(value["equals"])
    if "not_equals" in value:
        import aws_sdk_guardduty.types.not_equals

        out["notEquals"] = aws_sdk_guardduty.types.not_equals.serialize_json(
            value["not_equals"]
        )
    if "greater_than" in value:
        out["greaterThan"] = value["greater_than"]
    if "greater_than_or_equal" in value:
        out["greaterThanOrEqual"] = value["greater_than_or_equal"]
    if "less_than" in value:
        out["lessThan"] = value["less_than"]
    if "less_than_or_equal" in value:
        out["lessThanOrEqual"] = value["less_than_or_equal"]
    if "matches" in value:
        import aws_sdk_guardduty.types.matches

        out["matches"] = aws_sdk_guardduty.types.matches.serialize_json(
            value["matches"]
        )
    if "not_matches" in value:
        import aws_sdk_guardduty.types.not_matches

        out["notMatches"] = aws_sdk_guardduty.types.not_matches.serialize_json(
            value["not_matches"]
        )
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "eq" in data:
        import aws_sdk_guardduty.types.eq

        out["eq"] = aws_sdk_guardduty.types.eq.deserialize_json(data["eq"])
    if "neq" in data:
        import aws_sdk_guardduty.types.neq

        out["neq"] = aws_sdk_guardduty.types.neq.deserialize_json(data["neq"])
    if "gt" in data:
        out["gt"] = data["gt"]
    if "gte" in data:
        out["gte"] = data["gte"]
    if "lt" in data:
        out["lt"] = data["lt"]
    if "lte" in data:
        out["lte"] = data["lte"]
    if "equals" in data:
        import aws_sdk_guardduty.types.equals

        out["equals"] = aws_sdk_guardduty.types.equals.deserialize_json(data["equals"])
    if "notEquals" in data:
        import aws_sdk_guardduty.types.not_equals

        out["not_equals"] = aws_sdk_guardduty.types.not_equals.deserialize_json(
            data["notEquals"]
        )
    if "greaterThan" in data:
        out["greater_than"] = data["greaterThan"]
    if "greaterThanOrEqual" in data:
        out["greater_than_or_equal"] = data["greaterThanOrEqual"]
    if "lessThan" in data:
        out["less_than"] = data["lessThan"]
    if "lessThanOrEqual" in data:
        out["less_than_or_equal"] = data["lessThanOrEqual"]
    if "matches" in data:
        import aws_sdk_guardduty.types.matches

        out["matches"] = aws_sdk_guardduty.types.matches.deserialize_json(
            data["matches"]
        )
    if "notMatches" in data:
        import aws_sdk_guardduty.types.not_matches

        out["not_matches"] = aws_sdk_guardduty.types.not_matches.deserialize_json(
            data["notMatches"]
        )
    return out
