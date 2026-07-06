"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Period``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.boolean
    import aws_sdk_customer_profiles.types.max_size60
    import aws_sdk_customer_profiles.types.max_size1000
    import aws_sdk_customer_profiles.types.period_unit


class Period(TypedDict, closed=True):
    unit: "aws_sdk_customer_profiles.types.period_unit.PeriodUnit"
    """<p>The unit of time.</p>"""
    value: "aws_sdk_customer_profiles.types.max_size60.maxSize60"
    """<p>The amount of time of the specified unit.</p>"""
    max_invocations_per_profile: NotRequired[
        "aws_sdk_customer_profiles.types.max_size1000.maxSize1000"
    ]
    """<p>The maximum allowed number of destination invocations per profile.</p>"""
    unlimited: "aws_sdk_customer_profiles.types.boolean.boolean"
    """<p>If set to true, there is no limit on the number of destination invocations per profile. The default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Period) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.period_unit

    out["Unit"] = aws_sdk_customer_profiles.types.period_unit.serialize_json(
        value["unit"]
    )
    out["Value"] = value["value"]
    if "max_invocations_per_profile" in value:
        out["MaxInvocationsPerProfile"] = value["max_invocations_per_profile"]
    out["Unlimited"] = value.get("unlimited", False)
    return out


def deserialize_json(data: dict) -> Period:
    out: Period = {}  # type: ignore[typeddict-item]
    if "Unit" in data:
        import aws_sdk_customer_profiles.types.period_unit

        out["unit"] = aws_sdk_customer_profiles.types.period_unit.deserialize_json(
            data["Unit"]
        )
    else:
        raise DeserializationError("Period.unit required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Period.value required")
    if "MaxInvocationsPerProfile" in data:
        out["max_invocations_per_profile"] = data["MaxInvocationsPerProfile"]
    if "Unlimited" in data:
        out["unlimited"] = data["Unlimited"]
    else:
        out["unlimited"] = False
    return out
