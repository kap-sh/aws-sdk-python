"""Generated from Smithy shape ``com.amazonaws.snowball#CreateLongTermPricingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import capo_snowball.types.java_boolean
    import capo_snowball.types.long_term_pricing_type
    import capo_snowball.types.snowball_type


class CreateLongTermPricingRequest(TypedDict, closed=True):
    long_term_pricing_type: (
        "capo_snowball.types.long_term_pricing_type.LongTermPricingType"
    )
    """<p>The type of long-term pricing option you want for the device, either 1-year or 3-year long-term pricing.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "capo_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>Specifies whether the current long-term pricing type for the device should be renewed.</p>"""
    snowball_type: "capo_snowball.types.snowball_type.SnowballType"
    """<p>The type of Snow Family devices to use for the long-term pricing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLongTermPricingRequest) -> dict:
    out: dict = {}
    import capo_snowball.types.long_term_pricing_type

    out["LongTermPricingType"] = (
        capo_snowball.types.long_term_pricing_type.serialize_aws_json_1_1(
            value["long_term_pricing_type"]
        )
    )
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    import capo_snowball.types.snowball_type

    out["SnowballType"] = capo_snowball.types.snowball_type.serialize_aws_json_1_1(
        value["snowball_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLongTermPricingRequest:
    out: CreateLongTermPricingRequest = {}  # type: ignore[typeddict-item]
    if "LongTermPricingType" in data:
        import capo_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            capo_snowball.types.long_term_pricing_type.deserialize_aws_json_1_1(
                data["LongTermPricingType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLongTermPricingRequest.long_term_pricing_type required"
        )
    if "IsLongTermPricingAutoRenew" in data:
        out["is_long_term_pricing_auto_renew"] = data["IsLongTermPricingAutoRenew"]
    if "SnowballType" in data:
        import capo_snowball.types.snowball_type

        out["snowball_type"] = (
            capo_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLongTermPricingRequest.snowball_type required"
        )
    return out
