"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DomainNetworkSettings``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.subnets

class DomainNetworkSettings(TypedDict):
    subnets: "aws_sdk_license_manager_user_subscriptions.types.subnets.Subnets"
    """<p>Contains a list of subnets that apply for the Active Directory domain.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DomainNetworkSettings) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.subnets
    out["Subnets"] = aws_sdk_license_manager_user_subscriptions.types.subnets.serialize_json(value["subnets"])
    return out


def deserialize_json(data: dict) -> DomainNetworkSettings:
    out: DomainNetworkSettings = {}  # type: ignore[typeddict-item]
    if "Subnets" in data:
        import aws_sdk_license_manager_user_subscriptions.types.subnets
        out["subnets"] = aws_sdk_license_manager_user_subscriptions.types.subnets.deserialize_json(data["Subnets"])
    else:
        raise DeserializationError("DomainNetworkSettings.subnets required")
    return out