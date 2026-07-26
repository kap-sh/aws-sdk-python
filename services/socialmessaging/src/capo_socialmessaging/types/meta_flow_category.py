"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowCategory``."""

from typing import Literal, TypeAlias, cast

"""<p>The category that classifies the business purpose of a WhatsApp Flow.</p>"""
MetaFlowCategory: TypeAlias = Literal[
    "SIGN_UP",
    "SIGN_IN",
    "APPOINTMENT_BOOKING",
    "LEAD_GENERATION",
    "SHOPPING",
    "CONTACT_US",
    "CUSTOMER_SUPPORT",
    "SURVEY",
    "OTHER",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowCategory) -> str:
    return value


def deserialize_json(data: str) -> MetaFlowCategory:
    return cast(MetaFlowCategory, data)
