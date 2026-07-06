"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AddProfileKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.request_value_list
    import aws_sdk_customer_profiles.types.uuid


class AddProfileKeyRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    key_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile. The predefined keys you can use include: _account, _profileId, _assetId, _caseId, _orderId, _fullName, _phone, _email, _ctrContactId, _marketoLeadId, _salesforceAccountId, _salesforceContactId, _salesforceAssetId, _zendeskUserId, _zendeskExternalId, _zendeskTicketId, _serviceNowSystemId, _serviceNowIncidentId, _segmentUserId, _shopifyCustomerId, _shopifyOrderId.</p>"""
    values: "aws_sdk_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddProfileKeyRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["KeyName"] = value["key_name"]
    import aws_sdk_customer_profiles.types.request_value_list

    out["Values"] = aws_sdk_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> AddProfileKeyRequest:
    out: AddProfileKeyRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("AddProfileKeyRequest.profile_id required")
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("AddProfileKeyRequest.key_name required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.request_value_list

        out["values"] = (
            aws_sdk_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("AddProfileKeyRequest.values required")
    return out
