"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FreeTrialPricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.grant_list
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class FreeTrialPricingTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    duration: NotRequired[
        "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration of the free trial period.</p>"""
    grants: "aws_sdk_marketplace_discovery.types.grant_list.GrantList"
    """<p>The entitlements granted to the buyer during the free trial.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    if "duration" in value:
        out["duration"] = value["duration"]
    import aws_sdk_marketplace_discovery.types.grant_list

    out["grants"] = aws_sdk_marketplace_discovery.types.grant_list.serialize_json(
        value["grants"]
    )
    return out


def deserialize_json(data: dict) -> FreeTrialPricingTerm:
    out: FreeTrialPricingTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FreeTrialPricingTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FreeTrialPricingTerm.type required")
    if "duration" in data:
        out["duration"] = data["duration"]
    if "grants" in data:
        import aws_sdk_marketplace_discovery.types.grant_list

        out["grants"] = aws_sdk_marketplace_discovery.types.grant_list.deserialize_json(
            data["grants"]
        )
    else:
        raise DeserializationError("FreeTrialPricingTerm.grants required")
    return out
