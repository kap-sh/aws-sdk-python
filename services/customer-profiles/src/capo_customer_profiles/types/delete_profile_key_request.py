"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.request_value_list
    import capo_customer_profiles.types.uuid


class DeleteProfileKeyRequest(TypedDict, closed=True):
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    key_name: "capo_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile.</p>"""
    values: "capo_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileKeyRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["KeyName"] = value["key_name"]
    import capo_customer_profiles.types.request_value_list

    out["Values"] = capo_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> DeleteProfileKeyRequest:
    out: DeleteProfileKeyRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("DeleteProfileKeyRequest.profile_id required")
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("DeleteProfileKeyRequest.key_name required")
    if "Values" in data:
        import capo_customer_profiles.types.request_value_list

        out["values"] = (
            capo_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("DeleteProfileKeyRequest.values required")
    return out
