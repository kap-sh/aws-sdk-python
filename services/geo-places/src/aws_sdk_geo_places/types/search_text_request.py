"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.api_key
    import aws_sdk_geo_places.types.country_code
    import aws_sdk_geo_places.types.language_tag
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.search_text_additional_feature_list
    import aws_sdk_geo_places.types.search_text_filter
    import aws_sdk_geo_places.types.search_text_intended_use
    import aws_sdk_geo_places.types.sensitive_string
    import aws_sdk_geo_places.types.token


class SearchTextRequest(TypedDict, closed=True):
    query_text: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>Exactly one of the following fields must be set: <code>QueryText</code> or <code>QueryId</code>.</p> </note>"""
    query_id: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    r"""<p>The query Id returned by the suggest API. If passed in the request, the SearchText API will preform a SearchText query with the improved query terms for the original query made to the suggest API. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <note> <p>Exactly one of the following fields must be set: <code>QueryText</code> or <code>QueryId</code>.</p> </note>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>"""
    bias_position: NotRequired["aws_sdk_geo_places.types.position.Position"]
    """<p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>Exactly one of the following fields must be set: <code>BiasPosition</code>, <code>Filter.BoundingBox</code>, or <code>Filter.Circle</code>.</p> </note>"""
    filter: NotRequired["aws_sdk_geo_places.types.search_text_filter.SearchTextFilter"]
    """<p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>"""
    additional_features: NotRequired[
        "aws_sdk_geo_places.types.search_text_additional_feature_list.SearchTextAdditionalFeatureList"
    ]
    r"""<p>A list of optional additional parameters, such as time zone, that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>TimeZone</code> value.</p>"""
    language: NotRequired["aws_sdk_geo_places.types.language_tag.LanguageTag"]
    r"""<p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>"""
    political_view: NotRequired["aws_sdk_geo_places.types.country_code.CountryCode"]
    r"""<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p>"""
    intended_use: NotRequired[
        "aws_sdk_geo_places.types.search_text_intended_use.SearchTextIntendedUse"
    ]
    r"""<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). </p> <note> <p>When storing <code>SearchText</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>"""
    next_token: NotRequired["aws_sdk_geo_places.types.token.Token"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>"""
    key: NotRequired["aws_sdk_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextRequest) -> dict:
    out: dict = {}
    if "query_text" in value:
        out["QueryText"] = value["query_text"]
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "bias_position" in value:
        import aws_sdk_geo_places.types.position

        out["BiasPosition"] = aws_sdk_geo_places.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter" in value:
        import aws_sdk_geo_places.types.search_text_filter

        out["Filter"] = aws_sdk_geo_places.types.search_text_filter.serialize_json(
            value["filter"]
        )
    if "additional_features" in value:
        import aws_sdk_geo_places.types.search_text_additional_feature_list

        out["AdditionalFeatures"] = (
            aws_sdk_geo_places.types.search_text_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intended_use" in value:
        out["IntendedUse"] = value["intended_use"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchTextRequest:
    out: SearchTextRequest = {}  # type: ignore[typeddict-item]
    if "QueryText" in data:
        out["query_text"] = data["QueryText"]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "BiasPosition" in data:
        import aws_sdk_geo_places.types.position

        out["bias_position"] = aws_sdk_geo_places.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if "Filter" in data:
        import aws_sdk_geo_places.types.search_text_filter

        out["filter"] = aws_sdk_geo_places.types.search_text_filter.deserialize_json(
            data["Filter"]
        )
    if "AdditionalFeatures" in data:
        import aws_sdk_geo_places.types.search_text_additional_feature_list

        out["additional_features"] = (
            aws_sdk_geo_places.types.search_text_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    if "Language" in data:
        out["language"] = data["Language"]
    if "PoliticalView" in data:
        out["political_view"] = data["PoliticalView"]
    if "IntendedUse" in data:
        out["intended_use"] = data["IntendedUse"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
