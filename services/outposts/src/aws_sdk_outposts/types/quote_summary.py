"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.account_id
    import aws_sdk_outposts.types.country_code
    import aws_sdk_outposts.types.iso8601_timestamp
    import aws_sdk_outposts.types.order_identifier
    import aws_sdk_outposts.types.outpost_arn
    import aws_sdk_outposts.types.payment_option_list
    import aws_sdk_outposts.types.payment_term_list
    import aws_sdk_outposts.types.quote_capacity_list
    import aws_sdk_outposts.types.quote_constraint_list
    import aws_sdk_outposts.types.quote_description
    import aws_sdk_outposts.types.quote_id
    import aws_sdk_outposts.types.quote_option_list
    import aws_sdk_outposts.types.quote_status
    import aws_sdk_outposts.types.status_message


class QuoteSummary(TypedDict):
    quote_id: NotRequired["aws_sdk_outposts.types.quote_id.QuoteId"]
    """<p>The ID of the quote.</p>"""
    account_id: NotRequired["aws_sdk_outposts.types.account_id.AccountId"]
    """<p>The ID of the account that owns the quote.</p>"""
    quote_status: NotRequired["aws_sdk_outposts.types.quote_status.QuoteStatus"]
    """<p>The status of the quote.</p>"""
    status_message: NotRequired["aws_sdk_outposts.types.status_message.StatusMessage"]
    """<p>A message about the status of the quote.</p>"""
    outpost_arn: NotRequired["aws_sdk_outposts.types.outpost_arn.OutpostArn"]
    """<p>The ARN of the Outpost associated with the quote.</p>"""
    country_code: NotRequired["aws_sdk_outposts.types.country_code.CountryCode"]
    """<p>The country code for the Outpost site location.</p>"""
    requested_capacities: NotRequired[
        "aws_sdk_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The capacity requirements specified in the quote request.</p>"""
    requested_constraints: NotRequired[
        "aws_sdk_outposts.types.quote_constraint_list.QuoteConstraintList"
    ]
    """<p>The physical constraints specified in the quote request.</p>"""
    requested_payment_options: NotRequired[
        "aws_sdk_outposts.types.payment_option_list.PaymentOptionList"
    ]
    """<p>The payment options specified in the quote request.</p>"""
    requested_payment_terms: NotRequired[
        "aws_sdk_outposts.types.payment_term_list.PaymentTermList"
    ]
    """<p>The payment terms specified in the quote request.</p>"""
    quote_options: NotRequired[
        "aws_sdk_outposts.types.quote_option_list.QuoteOptionList"
    ]
    """<p>The configuration and pricing options for the quote.</p>"""
    submitted_order_id: NotRequired[
        "aws_sdk_outposts.types.order_identifier.OrderIdentifier"
    ]
    """<p>The ID of the order submitted for the quote.</p>"""
    created_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date the quote was created.</p>"""
    expiration_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date the quote expires.</p>"""
    description: NotRequired[
        "aws_sdk_outposts.types.quote_description.QuoteDescription"
    ]
    """<p>The description of the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSummary) -> dict:
    out: dict = {}
    if "quote_id" in value:
        out["QuoteId"] = value["quote_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "quote_status" in value:
        import aws_sdk_outposts.types.quote_status

        out["QuoteStatus"] = aws_sdk_outposts.types.quote_status.serialize_json(
            value["quote_status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "requested_capacities" in value:
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
    if "quote_options" in value:
        import aws_sdk_outposts.types.quote_option_list

        out["QuoteOptions"] = aws_sdk_outposts.types.quote_option_list.serialize_json(
            value["quote_options"]
        )
    if "submitted_order_id" in value:
        out["SubmittedOrderId"] = value["submitted_order_id"]
    if "created_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["CreatedDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["created_date"]
        )
    if "expiration_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["ExpirationDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["expiration_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> QuoteSummary:
    out: QuoteSummary = {}  # type: ignore[typeddict-item]
    if "QuoteId" in data:
        out["quote_id"] = data["QuoteId"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "QuoteStatus" in data:
        import aws_sdk_outposts.types.quote_status

        out["quote_status"] = aws_sdk_outposts.types.quote_status.deserialize_json(
            data["QuoteStatus"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "RequestedCapacities" in data:
        import aws_sdk_outposts.types.quote_capacity_list

        out["requested_capacities"] = (
            aws_sdk_outposts.types.quote_capacity_list.deserialize_json(
                data["RequestedCapacities"]
            )
        )
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
    if "QuoteOptions" in data:
        import aws_sdk_outposts.types.quote_option_list

        out["quote_options"] = (
            aws_sdk_outposts.types.quote_option_list.deserialize_json(
                data["QuoteOptions"]
            )
        )
    if "SubmittedOrderId" in data:
        out["submitted_order_id"] = data["SubmittedOrderId"]
    if "CreatedDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["created_date"] = aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
            data["CreatedDate"]
        )
    if "ExpirationDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["expiration_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["ExpirationDate"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
