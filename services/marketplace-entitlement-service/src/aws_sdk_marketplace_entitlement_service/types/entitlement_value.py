"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#EntitlementValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_entitlement_service.types.boolean
    import aws_sdk_marketplace_entitlement_service.types.double
    import aws_sdk_marketplace_entitlement_service.types.integer
    import aws_sdk_marketplace_entitlement_service.types.string


class EntitlementValue(TypedDict, closed=True):
    integer_value: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.integer.Integer"
    ]
    """<p>The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set.</p>"""
    double_value: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.double.Double"
    ]
    """<p>The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set.</p>"""
    boolean_value: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.boolean.Boolean"
    ]
    """<p>The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set.</p>"""
    string_value: NotRequired[
        "aws_sdk_marketplace_entitlement_service.types.string.String"
    ]
    """<p>The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementValue) -> dict:
    out: dict = {}
    if "integer_value" in value:
        out["IntegerValue"] = value["integer_value"]
    if "double_value" in value:
        out["DoubleValue"] = value["double_value"]
    if "boolean_value" in value:
        out["BooleanValue"] = value["boolean_value"]
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementValue:
    out: EntitlementValue = {}  # type: ignore[typeddict-item]
    if "IntegerValue" in data:
        out["integer_value"] = data["IntegerValue"]
    if "DoubleValue" in data:
        out["double_value"] = data["DoubleValue"]
    if "BooleanValue" in data:
        out["boolean_value"] = data["BooleanValue"]
    if "StringValue" in data:
        out["string_value"] = data["StringValue"]
    return out
