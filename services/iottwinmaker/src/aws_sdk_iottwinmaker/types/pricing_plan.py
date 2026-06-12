"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PricingPlan``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.bundle_information
    import aws_sdk_iottwinmaker.types.long
    import aws_sdk_iottwinmaker.types.pricing_mode
    import aws_sdk_iottwinmaker.types.timestamp
    import aws_sdk_iottwinmaker.types.update_reason


class PricingPlan(TypedDict):
    billable_entity_count: NotRequired["aws_sdk_iottwinmaker.types.long.Long"]
    """<p>The billable entity count.</p>"""
    bundle_information: NotRequired[
        "aws_sdk_iottwinmaker.types.bundle_information.BundleInformation"
    ]
    """<p>The pricing plan's bundle information.</p>"""
    effective_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The effective date and time of the pricing plan.</p>"""
    pricing_mode: "aws_sdk_iottwinmaker.types.pricing_mode.PricingMode"
    """<p>The pricing mode.</p>"""
    update_date_time: "aws_sdk_iottwinmaker.types.timestamp.Timestamp"
    """<p>The set date and time for updating a pricing plan.</p>"""
    update_reason: "aws_sdk_iottwinmaker.types.update_reason.UpdateReason"
    """<p>The update reason for changing a pricing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlan) -> dict:
    out: dict = {}
    if "billable_entity_count" in value:
        out["billableEntityCount"] = value["billable_entity_count"]
    if "bundle_information" in value:
        import aws_sdk_iottwinmaker.types.bundle_information

        out["bundleInformation"] = (
            aws_sdk_iottwinmaker.types.bundle_information.serialize_json(
                value["bundle_information"]
            )
        )
    import aws_sdk_iottwinmaker.types.timestamp

    out["effectiveDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["effective_date_time"]
    )
    out["pricingMode"] = value["pricing_mode"]
    import aws_sdk_iottwinmaker.types.timestamp

    out["updateDateTime"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    out["updateReason"] = value["update_reason"]
    return out


def deserialize_json(data: dict) -> PricingPlan:
    out: PricingPlan = {}  # type: ignore[typeddict-item]
    if "billableEntityCount" in data:
        out["billable_entity_count"] = data["billableEntityCount"]
    if "bundleInformation" in data:
        import aws_sdk_iottwinmaker.types.bundle_information

        out["bundle_information"] = (
            aws_sdk_iottwinmaker.types.bundle_information.deserialize_json(
                data["bundleInformation"]
            )
        )
    if "effectiveDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["effective_date_time"] = (
            aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
                data["effectiveDateTime"]
            )
        )
    else:
        raise DeserializationError("PricingPlan.effective_date_time required")
    if "pricingMode" in data:
        out["pricing_mode"] = data["pricingMode"]
    else:
        raise DeserializationError("PricingPlan.pricing_mode required")
    if "updateDateTime" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["update_date_time"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        raise DeserializationError("PricingPlan.update_date_time required")
    if "updateReason" in data:
        out["update_reason"] = data["updateReason"]
    else:
        raise DeserializationError("PricingPlan.update_reason required")
    return out
