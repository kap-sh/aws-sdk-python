"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileHistoryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.action_type
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.type_name
    import aws_sdk_customer_profiles.types.uuid


class ListProfileHistoryRecordsRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain for which to return profile history records.</p>"""
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The identifier of the profile to be taken.</p>"""
    object_type_name: NotRequired["aws_sdk_customer_profiles.types.type_name.typeName"]
    """<p>Applies a filter to include profile history records only with the specified <code>ObjectTypeName</code> value in the response.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of results to return per page.</p>"""
    action_type: NotRequired["aws_sdk_customer_profiles.types.action_type.ActionType"]
    """<p>Applies a filter to include profile history records only with the specified <code>ActionType</code> value in the response.</p>"""
    performed_by: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>Applies a filter to include profile history records only with the specified <code>PerformedBy</code> value in the response. The <code>PerformedBy</code> value can be the Amazon Resource Name (ARN) of the person or service principal who performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileHistoryRecordsRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "object_type_name" in value:
        out["ObjectTypeName"] = value["object_type_name"]
    if "action_type" in value:
        import aws_sdk_customer_profiles.types.action_type

        out["ActionType"] = aws_sdk_customer_profiles.types.action_type.serialize_json(
            value["action_type"]
        )
    if "performed_by" in value:
        out["PerformedBy"] = value["performed_by"]
    return out


def deserialize_json(data: dict) -> ListProfileHistoryRecordsRequest:
    out: ListProfileHistoryRecordsRequest = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError(
            "ListProfileHistoryRecordsRequest.profile_id required"
        )
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    if "ActionType" in data:
        import aws_sdk_customer_profiles.types.action_type

        out["action_type"] = (
            aws_sdk_customer_profiles.types.action_type.deserialize_json(
                data["ActionType"]
            )
        )
    if "PerformedBy" in data:
        out["performed_by"] = data["PerformedBy"]
    return out
