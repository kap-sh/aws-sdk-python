"""Generated from Smithy shape ``com.amazonaws.outposts#CreateQuoteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.country_code
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.payment_option_list
    import aws_sdk_outposts.types.payment_term_list
    import aws_sdk_outposts.types.quote_capacity_list
    import aws_sdk_outposts.types.quote_constraint_list
    import aws_sdk_outposts.types.quote_description


class CreateQuoteInput(TypedDict, closed=True):
    outpost_identifier: NotRequired[
        "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    ]
    """<p>The ID or ARN of the Outpost to associate with the quote. If not specified, the quote is created without an Outpost association.</p>"""
    country_code: "aws_sdk_outposts.types.country_code.CountryCode"
    """<p>The country code for the Outpost site location.</p>"""
    requested_capacities: "aws_sdk_outposts.types.quote_capacity_list.QuoteCapacityList"
    """<p>The capacity requirements for the quote. Each entry specifies a capacity type (such as Amazon EC2), the unit, and the quantity. For Amazon EC2, the quantity is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, the quantity is the total desired end-state capacity of the Outpost.</p>"""
    requested_constraints: NotRequired[
        "aws_sdk_outposts.types.quote_constraint_list.QuoteConstraintList"
    ]
    """<p>The physical constraints for the quote, such as maximum number of racks, maximum power draw per rack, or maximum weight per rack.</p>"""
    requested_payment_options: NotRequired[
        "aws_sdk_outposts.types.payment_option_list.PaymentOptionList"
    ]
    """<p>The payment options to include in the quote pricing. If not specified, all available payment options are returned.</p>"""
    requested_payment_terms: NotRequired[
        "aws_sdk_outposts.types.payment_term_list.PaymentTermList"
    ]
    """<p>The payment terms to include in the quote pricing. If not specified, all available payment terms are returned.</p>"""
    description: NotRequired[
        "aws_sdk_outposts.types.quote_description.QuoteDescription"
    ]
    """<p>A description for the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuoteInput) -> dict:
    out: dict = {}
    if "outpost_identifier" in value:
        out["OutpostIdentifier"] = value["outpost_identifier"]
    out["CountryCode"] = value["country_code"]
    import aws_sdk_outposts.types.quote_capacity_list

    out["RequestedCapacities"] = (
        aws_sdk_outposts.types.quote_capacity_list.serialize_json(
            value["requested_capacities"]
        )
    )
    if "requested_constraints" in value:
        import aws_sdk_outposts.types.quote_constraint_list

        out["RequestedConstraints"] = (
            aws_sdk_outposts.types.quote_constraint_list.serialize_json(
                value["requested_constraints"]
            )
        )
    if "requested_payment_options" in value:
        import aws_sdk_outposts.types.payment_option_list

        out["RequestedPaymentOptions"] = (
            aws_sdk_outposts.types.payment_option_list.serialize_json(
                value["requested_payment_options"]
            )
        )
    if "requested_payment_terms" in value:
        import aws_sdk_outposts.types.payment_term_list

        out["RequestedPaymentTerms"] = (
            aws_sdk_outposts.types.payment_term_list.serialize_json(
                value["requested_payment_terms"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateQuoteInput:
    out: CreateQuoteInput = {}  # type: ignore[typeddict-item]
    if "OutpostIdentifier" in data:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    else:
        raise DeserializationError("CreateQuoteInput.country_code required")
    if "RequestedCapacities" in data:
        import aws_sdk_outposts.types.quote_capacity_list

        out["requested_capacities"] = (
            aws_sdk_outposts.types.quote_capacity_list.deserialize_json(
                data["RequestedCapacities"]
            )
        )
    else:
        raise DeserializationError("CreateQuoteInput.requested_capacities required")
    if "RequestedConstraints" in data:
        import aws_sdk_outposts.types.quote_constraint_list

        out["requested_constraints"] = (
            aws_sdk_outposts.types.quote_constraint_list.deserialize_json(
                data["RequestedConstraints"]
            )
        )
    if "RequestedPaymentOptions" in data:
        import aws_sdk_outposts.types.payment_option_list

        out["requested_payment_options"] = (
            aws_sdk_outposts.types.payment_option_list.deserialize_json(
                data["RequestedPaymentOptions"]
            )
        )
    if "RequestedPaymentTerms" in data:
        import aws_sdk_outposts.types.payment_term_list

        out["requested_payment_terms"] = (
            aws_sdk_outposts.types.payment_term_list.deserialize_json(
                data["RequestedPaymentTerms"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
