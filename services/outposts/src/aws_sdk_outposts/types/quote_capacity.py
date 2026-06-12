"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteCapacity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.nullable_float
    import aws_sdk_outposts.types.quote_capacity_type
    import aws_sdk_outposts.types.string


class QuoteCapacity(TypedDict):
    quote_capacity_type: NotRequired[
        "aws_sdk_outposts.types.quote_capacity_type.QuoteCapacityType"
    ]
    """<p>The type of capacity. Valid values are <code>EC2</code>, <code>EBS</code>, and <code>S3</code>.</p>"""
    unit: NotRequired["aws_sdk_outposts.types.string.String"]
    """<p>The unit of measurement for the capacity. For Amazon EC2, this is the instance type (for example, <code>c5.24xlarge</code>). For Amazon EBS and Amazon S3, this is the storage unit (for example, <code>TiB</code> for tebibytes).</p>"""
    quantity: NotRequired["aws_sdk_outposts.types.nullable_float.NullableFloat"]
    """<p>The quantity of the specified capacity unit. For Amazon EC2, this is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, this is the total desired end-state capacity of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteCapacity) -> dict:
    out: dict = {}
    if "quote_capacity_type" in value:
        import aws_sdk_outposts.types.quote_capacity_type

        out["QuoteCapacityType"] = (
            aws_sdk_outposts.types.quote_capacity_type.serialize_json(
                value["quote_capacity_type"]
            )
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> QuoteCapacity:
    out: QuoteCapacity = {}  # type: ignore[typeddict-item]
    if "QuoteCapacityType" in data:
        import aws_sdk_outposts.types.quote_capacity_type

        out["quote_capacity_type"] = (
            aws_sdk_outposts.types.quote_capacity_type.deserialize_json(
                data["QuoteCapacityType"]
            )
        )
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    return out
