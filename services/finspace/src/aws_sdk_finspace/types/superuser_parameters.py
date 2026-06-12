"""Generated from Smithy shape ``com.amazonaws.finspace#SuperuserParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.email_id
    import aws_sdk_finspace.types.name_string


class SuperuserParameters(TypedDict):
    email_address: "aws_sdk_finspace.types.email_id.EmailId"
    """<p>The email address of the superuser.</p>"""
    first_name: "aws_sdk_finspace.types.name_string.NameString"
    """<p>The first name of the superuser.</p>"""
    last_name: "aws_sdk_finspace.types.name_string.NameString"
    """<p>The last name of the superuser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuperuserParameters) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    out["firstName"] = value["first_name"]
    out["lastName"] = value["last_name"]
    return out


def deserialize_json(data: dict) -> SuperuserParameters:
    out: SuperuserParameters = {}  # type: ignore[typeddict-item]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    else:
        raise DeserializationError("SuperuserParameters.email_address required")
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    else:
        raise DeserializationError("SuperuserParameters.first_name required")
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    else:
        raise DeserializationError("SuperuserParameters.last_name required")
    return out
