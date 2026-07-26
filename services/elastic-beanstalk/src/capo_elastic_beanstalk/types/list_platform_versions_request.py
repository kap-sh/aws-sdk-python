"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListPlatformVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_filters
    import capo_elastic_beanstalk.types.platform_max_records
    import capo_elastic_beanstalk.types.token


class ListPlatformVersionsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_elastic_beanstalk.types.platform_filters.PlatformFilters"
    ]
    """<p>Criteria for restricting the resulting list of platform versions. The filter is interpreted as a logical conjunction (AND) of the separate <code>PlatformFilter</code> terms.</p>"""
    max_records: NotRequired[
        "capo_elastic_beanstalk.types.platform_max_records.PlatformMaxRecords"
    ]
    """<p>The maximum number of platform version values returned in one call.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformVersionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filters" in value:
        import capo_elastic_beanstalk.types.platform_filters

        capo_elastic_beanstalk.types.platform_filters.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformVersionsRequest:
    out: ListPlatformVersionsRequest = {}  # type: ignore[typeddict-item]
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_elastic_beanstalk.types.platform_filters

        out["filters"] = (
            capo_elastic_beanstalk.types.platform_filters.deserialize_query(
                child_filters
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
