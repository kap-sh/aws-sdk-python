"""Generated from Smithy shape ``com.amazonaws.sesv2#ResourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of resource that can be associated with a tenant. Can be one of the following:</p> <ul> <li> <p> <code>EMAIL_IDENTITY</code> - An email address or domain that you use to send email.</p> </li> <li> <p> <code>CONFIGURATION_SET</code> - A set of rules that you can apply to emails you send.</p> </li> <li> <p> <code>EMAIL_TEMPLATE</code> - A template that defines the content of an email message.</p> </li> </ul>"""
ResourceType: TypeAlias = Literal[
    "EMAIL_IDENTITY",
    "CONFIGURATION_SET",
    "EMAIL_TEMPLATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
