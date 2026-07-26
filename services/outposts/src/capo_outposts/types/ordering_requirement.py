"""Generated from Smithy shape ``com.amazonaws.outposts#OrderingRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.ordering_requirement_status
    import capo_outposts.types.ordering_requirement_type
    import capo_outposts.types.status_message


class OrderingRequirement(TypedDict, closed=True):
    status_message: NotRequired["capo_outposts.types.status_message.StatusMessage"]
    """<p>A message about the ordering requirement.</p>"""
    ordering_requirement_type: NotRequired[
        "capo_outposts.types.ordering_requirement_type.OrderingRequirementType"
    ]
    """<p>The type of ordering requirement. Indicates which check failed or passed.</p> <ul> <li> <p> <code>OUTPOST_ACTIVE_CHECK_ERROR</code> - The Outpost must be in an active state.</p> </li> <li> <p> <code>MAXIMUM_ALLOWED_ORDERS_CHECK_ERROR</code> - The maximum number of allowed orders has been reached.</p> </li> <li> <p> <code>VALID_ZIP_CODE_CHECK_ERROR</code> - The site address must have a valid zip code.</p> </li> <li> <p> <code>RACK_PHYSICAL_PROPERTIES_CHECK_ERROR</code> - The rack physical properties do not meet requirements.</p> </li> <li> <p> <code>OPERATING_ADDRESS_EXISTENCE_CHECK_ERROR</code> - The site must have an operating address.</p> </li> <li> <p> <code>SHIPPING_ADDRESS_EXISTENCE_CHECK_ERROR</code> - The site must have a shipping address.</p> </li> <li> <p> <code>COUNTRY_CODE_MISMATCH_CHECK_ERROR</code> - The country code on the quote does not match the Outpost site country.</p> </li> <li> <p> <code>OUTPOST_GENERATION_MISMATCH_ERROR</code> - The Outpost generation does not match the requested configuration.</p> </li> <li> <p> <code>OUTPOST_ID_MISSING_ON_QUOTE_ERROR</code> - The quote must be associated with an Outpost before submitting an order.</p> </li> <li> <p> <code>ENTERPRISE_SUPPORT_ERROR</code> - Enterprise Support is required.</p> </li> <li> <p> <code>SHIPPING_ADDRESS_MISSING_CONTACT_NAME_ERROR</code> - The shipping address must have a contact name.</p> </li> <li> <p> <code>SHIPPING_ADDRESS_MISSING_CONTACT_NUMBER_ERROR</code> - The shipping address must have a contact phone number.</p> </li> <li> <p> <code>SHIPPING_ADDRESS_MISSING_CONTACT_INFO_ERROR</code> - The shipping address must have contact information.</p> </li> <li> <p> <code>OUTPOST_STATE_CHANGED_ERROR</code> - The Outpost state has changed since the quote was created.</p> </li> <li> <p> <code>OUTPOST_NOT_FOUND_ERROR</code> - The Outpost associated with the quote was not found.</p> </li> <li> <p> <code>OUTPOST_RENEWAL_REQUIRED_ERROR</code> - The Outpost requires a renewal before a new order can be submitted.</p> </li> <li> <p> <code>UNSUPPORTED</code> - The requirement type is not recognized.</p> </li> </ul>"""
    status: NotRequired[
        "capo_outposts.types.ordering_requirement_status.OrderingRequirementStatus"
    ]
    """<p>The status of the ordering requirement. Valid values are <code>PASS</code>, <code>FAIL</code>, and <code>EXEMPT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrderingRequirement) -> dict:
    out: dict = {}
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "ordering_requirement_type" in value:
        import capo_outposts.types.ordering_requirement_type

        out["OrderingRequirementType"] = (
            capo_outposts.types.ordering_requirement_type.serialize_json(
                value["ordering_requirement_type"]
            )
        )
    if "status" in value:
        import capo_outposts.types.ordering_requirement_status

        out["Status"] = capo_outposts.types.ordering_requirement_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> OrderingRequirement:
    out: OrderingRequirement = {}  # type: ignore[typeddict-item]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "OrderingRequirementType" in data:
        import capo_outposts.types.ordering_requirement_type

        out["ordering_requirement_type"] = (
            capo_outposts.types.ordering_requirement_type.deserialize_json(
                data["OrderingRequirementType"]
            )
        )
    if "Status" in data:
        import capo_outposts.types.ordering_requirement_status

        out["status"] = (
            capo_outposts.types.ordering_requirement_status.deserialize_json(
                data["Status"]
            )
        )
    return out
