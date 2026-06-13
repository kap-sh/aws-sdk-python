"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Constraints``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.rate_card_constraint_type


class Constraints(TypedDict):
    multiple_dimension_selection: "aws_sdk_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType"
    """<p>Whether the buyer can select multiple dimensions. Values are <code>Allowed</code> or <code>Disallowed</code>.</p>"""
    quantity_configuration: "aws_sdk_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType"
    """<p>Whether the buyer can configure quantities. Values are <code>Allowed</code> or <code>Disallowed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Constraints) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.rate_card_constraint_type

    out["multipleDimensionSelection"] = (
        aws_sdk_marketplace_discovery.types.rate_card_constraint_type.serialize_json(
            value["multiple_dimension_selection"]
        )
    )
    import aws_sdk_marketplace_discovery.types.rate_card_constraint_type

    out["quantityConfiguration"] = (
        aws_sdk_marketplace_discovery.types.rate_card_constraint_type.serialize_json(
            value["quantity_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> Constraints:
    out: Constraints = {}  # type: ignore[typeddict-item]
    if "multipleDimensionSelection" in data:
        import aws_sdk_marketplace_discovery.types.rate_card_constraint_type

        out["multiple_dimension_selection"] = (
            aws_sdk_marketplace_discovery.types.rate_card_constraint_type.deserialize_json(
                data["multipleDimensionSelection"]
            )
        )
    else:
        raise DeserializationError("Constraints.multiple_dimension_selection required")
    if "quantityConfiguration" in data:
        import aws_sdk_marketplace_discovery.types.rate_card_constraint_type

        out["quantity_configuration"] = (
            aws_sdk_marketplace_discovery.types.rate_card_constraint_type.deserialize_json(
                data["quantityConfiguration"]
            )
        )
    else:
        raise DeserializationError("Constraints.quantity_configuration required")
    return out
