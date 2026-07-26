"""Generated from Smithy shape ``com.amazonaws.iot#SecurityProfileIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.security_profile_arn
    import capo_iot.types.security_profile_name


class SecurityProfileIdentifier(TypedDict, closed=True):
    name: "capo_iot.types.security_profile_name.SecurityProfileName"
    """<p>The name you've given to the security profile.</p>"""
    arn: "capo_iot.types.security_profile_arn.SecurityProfileArn"
    """<p>The ARN of the security profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileIdentifier) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SecurityProfileIdentifier:
    out: SecurityProfileIdentifier = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SecurityProfileIdentifier.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SecurityProfileIdentifier.arn required")
    return out
