"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.request_value_list
    import aws_sdk_customer_profiles.types.uuid


class DeleteProfileKeyRequest(TypedDict):
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    key_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile.</p>"""
    values: "aws_sdk_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileKeyRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["KeyName"] = value["key_name"]
    import aws_sdk_customer_profiles.types.request_value_list

    out["Values"] = aws_sdk_customer_profiles.types.request_value_list.serialize_json(
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
        import aws_sdk_customer_profiles.types.request_value_list

        out["values"] = (
            aws_sdk_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("DeleteProfileKeyRequest.values required")
    return out
