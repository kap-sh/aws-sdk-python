"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSimilarProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.match_type
    import aws_sdk_customer_profiles.types.max_size100
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.token


class GetSimilarProfilesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous <code>GetSimilarProfiles</code> API call.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    match_type: "aws_sdk_customer_profiles.types.match_type.MatchType"
    """<p>Specify the type of matching to get similar profiles for.</p>"""
    search_key: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The string indicating the search key to be used.</p>"""
    search_value: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The string based on <code>SearchKey</code> to be searched for similar profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSimilarProfilesRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.match_type

    out["MatchType"] = aws_sdk_customer_profiles.types.match_type.serialize_json(
        value["match_type"]
    )
    out["SearchKey"] = value["search_key"]
    out["SearchValue"] = value["search_value"]
    return out


def deserialize_json(data: dict) -> GetSimilarProfilesRequest:
    out: GetSimilarProfilesRequest = {}  # type: ignore[typeddict-item]
    if "MatchType" in data:
        import aws_sdk_customer_profiles.types.match_type

        out["match_type"] = aws_sdk_customer_profiles.types.match_type.deserialize_json(
            data["MatchType"]
        )
    else:
        raise DeserializationError("GetSimilarProfilesRequest.match_type required")
    if "SearchKey" in data:
        out["search_key"] = data["SearchKey"]
    else:
        raise DeserializationError("GetSimilarProfilesRequest.search_key required")
    if "SearchValue" in data:
        out["search_value"] = data["SearchValue"]
    else:
        raise DeserializationError("GetSimilarProfilesRequest.search_value required")
    return out
