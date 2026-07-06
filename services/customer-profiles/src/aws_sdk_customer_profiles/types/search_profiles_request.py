"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SearchProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.additional_search_keys_list
    import aws_sdk_customer_profiles.types.logical_operator
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.request_value_list
    import aws_sdk_customer_profiles.types.token


class SearchProfilesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous SearchProfiles API call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p> <p>The default is 20 if this parameter is not included in the request.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    key_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>A searchable identifier of a customer profile. The predefined keys you can use to search include: _account, _profileId, _assetId, _caseId, _orderId, _fullName, _phone, _email, _ctrContactId, _marketoLeadId, _salesforceAccountId, _salesforceContactId, _salesforceAssetId, _zendeskUserId, _zendeskExternalId, _zendeskTicketId, _serviceNowSystemId, _serviceNowIncidentId, _segmentUserId, _shopifyCustomerId, _shopifyOrderId.</p>"""
    values: "aws_sdk_customer_profiles.types.request_value_list.requestValueList"
    """<p>A list of key values.</p>"""
    additional_search_keys: NotRequired[
        "aws_sdk_customer_profiles.types.additional_search_keys_list.additionalSearchKeysList"
    ]
    """<p>A list of <code>AdditionalSearchKey</code> objects that are each searchable identifiers of a profile. Each <code>AdditionalSearchKey</code> object contains a <code>KeyName</code> and a list of <code>Values</code> associated with that specific key (i.e., a key-value(s) pair). These additional search keys will be used in conjunction with the <code>LogicalOperator</code> and the required <code>KeyName</code> and <code>Values</code> parameters to search for profiles that satisfy the search criteria. </p>"""
    logical_operator: NotRequired[
        "aws_sdk_customer_profiles.types.logical_operator.logicalOperator"
    ]
    """<p>Relationship between all specified search keys that will be used to search for profiles. This includes the required <code>KeyName</code> and <code>Values</code> parameters as well as any key-value(s) pairs specified in the <code>AdditionalSearchKeys</code> list.</p> <p>This parameter influences which profiles will be returned in the response in the following manner:</p> <ul> <li> <p> <code>AND</code> - The response only includes profiles that match all of the search keys.</p> </li> <li> <p> <code>OR</code> - The response includes profiles that match at least one of the search keys.</p> </li> </ul> <p>The <code>OR</code> relationship is the default behavior if this parameter is not included in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchProfilesRequest) -> dict:
    out: dict = {}
    out["KeyName"] = value["key_name"]
    import aws_sdk_customer_profiles.types.request_value_list

    out["Values"] = aws_sdk_customer_profiles.types.request_value_list.serialize_json(
        value["values"]
    )
    if "additional_search_keys" in value:
        import aws_sdk_customer_profiles.types.additional_search_keys_list

        out["AdditionalSearchKeys"] = (
            aws_sdk_customer_profiles.types.additional_search_keys_list.serialize_json(
                value["additional_search_keys"]
            )
        )
    if "logical_operator" in value:
        import aws_sdk_customer_profiles.types.logical_operator

        out["LogicalOperator"] = (
            aws_sdk_customer_profiles.types.logical_operator.serialize_json(
                value["logical_operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchProfilesRequest:
    out: SearchProfilesRequest = {}  # type: ignore[typeddict-item]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    else:
        raise DeserializationError("SearchProfilesRequest.key_name required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.request_value_list

        out["values"] = (
            aws_sdk_customer_profiles.types.request_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("SearchProfilesRequest.values required")
    if "AdditionalSearchKeys" in data:
        import aws_sdk_customer_profiles.types.additional_search_keys_list

        out["additional_search_keys"] = (
            aws_sdk_customer_profiles.types.additional_search_keys_list.deserialize_json(
                data["AdditionalSearchKeys"]
            )
        )
    if "LogicalOperator" in data:
        import aws_sdk_customer_profiles.types.logical_operator

        out["logical_operator"] = (
            aws_sdk_customer_profiles.types.logical_operator.deserialize_json(
                data["LogicalOperator"]
            )
        )
    return out
