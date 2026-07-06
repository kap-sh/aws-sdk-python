"""Generated from Smithy shape ``com.amazonaws.iotevents#SSOIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.identity_store_id
    import aws_sdk_iot_events.types.sso_reference_id


class SSOIdentity(TypedDict, closed=True):
    identity_store_id: "aws_sdk_iot_events.types.identity_store_id.IdentityStoreId"
    """<p>The ID of the AWS SSO identity store.</p>"""
    user_id: NotRequired["aws_sdk_iot_events.types.sso_reference_id.SSOReferenceId"]
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SSOIdentity) -> dict:
    out: dict = {}
    out["identityStoreId"] = value["identity_store_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> SSOIdentity:
    out: SSOIdentity = {}  # type: ignore[typeddict-item]
    if "identityStoreId" in data:
        out["identity_store_id"] = data["identityStoreId"]
    else:
        raise DeserializationError("SSOIdentity.identity_store_id required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
