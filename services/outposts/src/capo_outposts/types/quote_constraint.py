"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.constraint_value
    import capo_outposts.types.quote_constraint_type


class QuoteConstraint(TypedDict, closed=True):
    quote_constraint_type: NotRequired[
        "capo_outposts.types.quote_constraint_type.QuoteConstraintType"
    ]
    """<p>The type of constraint. Valid values are <code>RACK_MAXIMUM</code>, <code>RACK_MAX_POWER_KVA</code>, and <code>RACK_MAX_WEIGHT_LBS</code>.</p>"""
    value: NotRequired["capo_outposts.types.constraint_value.ConstraintValue"]
    """<p>The value of the constraint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteConstraint) -> dict:
    out: dict = {}
    if "quote_constraint_type" in value:
        import capo_outposts.types.quote_constraint_type

        out["QuoteConstraintType"] = (
            capo_outposts.types.quote_constraint_type.serialize_json(
                value["quote_constraint_type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> QuoteConstraint:
    out: QuoteConstraint = {}  # type: ignore[typeddict-item]
    if "QuoteConstraintType" in data:
        import capo_outposts.types.quote_constraint_type

        out["quote_constraint_type"] = (
            capo_outposts.types.quote_constraint_type.deserialize_json(
                data["QuoteConstraintType"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
