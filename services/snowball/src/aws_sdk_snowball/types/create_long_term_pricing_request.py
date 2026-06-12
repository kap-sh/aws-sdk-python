"""Generated from Smithy shape ``com.amazonaws.snowball#CreateLongTermPricingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.java_boolean
    import aws_sdk_snowball.types.long_term_pricing_type
    import aws_sdk_snowball.types.snowball_type


class CreateLongTermPricingRequest(TypedDict):
    long_term_pricing_type: (
        "aws_sdk_snowball.types.long_term_pricing_type.LongTermPricingType"
    )
    """<p>The type of long-term pricing option you want for the device, either 1-year or 3-year long-term pricing.</p>"""
    is_long_term_pricing_auto_renew: NotRequired[
        "aws_sdk_snowball.types.java_boolean.JavaBoolean"
    ]
    """<p>Specifies whether the current long-term pricing type for the device should be renewed.</p>"""
    snowball_type: "aws_sdk_snowball.types.snowball_type.SnowballType"
    """<p>The type of Snow Family devices to use for the long-term pricing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLongTermPricingRequest) -> dict:
    out: dict = {}
    import aws_sdk_snowball.types.long_term_pricing_type

    out["LongTermPricingType"] = (
        aws_sdk_snowball.types.long_term_pricing_type.serialize_aws_json_1_1(
            value["long_term_pricing_type"]
        )
    )
    if "is_long_term_pricing_auto_renew" in value:
        out["IsLongTermPricingAutoRenew"] = value["is_long_term_pricing_auto_renew"]
    import aws_sdk_snowball.types.snowball_type

    out["SnowballType"] = aws_sdk_snowball.types.snowball_type.serialize_aws_json_1_1(
        value["snowball_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLongTermPricingRequest:
    out: CreateLongTermPricingRequest = {}  # type: ignore[typeddict-item]
    if "LongTermPricingType" in data:
        import aws_sdk_snowball.types.long_term_pricing_type

        out["long_term_pricing_type"] = (
            aws_sdk_snowball.types.long_term_pricing_type.deserialize_aws_json_1_1(
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
        import aws_sdk_snowball.types.snowball_type

        out["snowball_type"] = (
            aws_sdk_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLongTermPricingRequest.snowball_type required"
        )
    return out
