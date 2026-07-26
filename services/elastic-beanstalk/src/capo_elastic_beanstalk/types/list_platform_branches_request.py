"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListPlatformBranchesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_branch_max_records
    import capo_elastic_beanstalk.types.search_filters
    import capo_elastic_beanstalk.types.token


class ListPlatformBranchesRequest(TypedDict, closed=True):
    filters: NotRequired["capo_elastic_beanstalk.types.search_filters.SearchFilters"]
    """<p>Criteria for restricting the resulting list of platform branches. The filter is evaluated as a logical conjunction (AND) of the separate <code>SearchFilter</code> terms.</p> <p>The following list shows valid attribute values for each of the <code>SearchFilter</code> terms. Most operators take a single value. The <code>in</code> and <code>not_in</code> operators can take multiple values.</p> <ul> <li> <p> <code>Attribute = BranchName</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>begins_with</code> | <code>ends_with</code> | <code>contains</code> | <code>in</code> | <code>not_in</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = LifecycleState</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>in</code> | <code>not_in</code> </p> </li> <li> <p> <code>Values</code>: <code>beta</code> | <code>supported</code> | <code>deprecated</code> | <code>retired</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = PlatformName</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> | <code>begins_with</code> | <code>ends_with</code> | <code>contains</code> | <code>in</code> | <code>not_in</code> </p> </li> </ul> </li> <li> <p> <code>Attribute = TierType</code>:</p> <ul> <li> <p> <code>Operator</code>: <code>=</code> | <code>!=</code> </p> </li> <li> <p> <code>Values</code>: <code>WebServer/Standard</code> | <code>Worker/SQS/HTTP</code> </p> </li> </ul> </li> </ul> <p>Array size: limited to 10 <code>SearchFilter</code> objects.</p> <p>Within each <code>SearchFilter</code> item, the <code>Values</code> array is limited to 10 items.</p>"""
    max_records: NotRequired[
        "capo_elastic_beanstalk.types.platform_branch_max_records.PlatformBranchMaxRecords"
    ]
    """<p>The maximum number of platform branch values returned in one call.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.token.Token"]
    """<p>For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If no <code>NextToken</code> is specified, the first page is retrieved.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformBranchesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "filters" in value:
        import capo_elastic_beanstalk.types.search_filters

        capo_elastic_beanstalk.types.search_filters.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformBranchesRequest:
    out: ListPlatformBranchesRequest = {}  # type: ignore[typeddict-item]
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_elastic_beanstalk.types.search_filters

        out["filters"] = capo_elastic_beanstalk.types.search_filters.deserialize_query(
            child_filters
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
