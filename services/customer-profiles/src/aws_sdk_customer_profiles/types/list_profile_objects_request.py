"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.object_filter
    import aws_sdk_customer_profiles.types.token
    import aws_sdk_customer_profiles.types.type_name
    import aws_sdk_customer_profiles.types.uuid


class ListProfileObjectsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListProfileObjects.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""
    object_filter: NotRequired[
        "aws_sdk_customer_profiles.types.object_filter.ObjectFilter"
    ]
    """<p>Applies a filter to the response to include profile objects with the specified index values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectsRequest) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    out["ProfileId"] = value["profile_id"]
    if "object_filter" in value:
        import aws_sdk_customer_profiles.types.object_filter

        out["ObjectFilter"] = (
            aws_sdk_customer_profiles.types.object_filter.serialize_json(
                value["object_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListProfileObjectsRequest:
    out: ListProfileObjectsRequest = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "ListProfileObjectsRequest.object_type_name required"
        )
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("ListProfileObjectsRequest.profile_id required")
    if "ObjectFilter" in data:
        import aws_sdk_customer_profiles.types.object_filter

        out["object_filter"] = (
            aws_sdk_customer_profiles.types.object_filter.deserialize_json(
                data["ObjectFilter"]
            )
        )
    return out
