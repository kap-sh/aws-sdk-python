"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaStatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_instance_sql_ha_states_request_max_results_integer
    import capo_ec2.types.filter_list
    import capo_ec2.types.instance_id_string_list
    import capo_ec2.types.next_token


class DescribeInstanceSqlHaStatesRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the SQL Server High Availability instances to describe. If omitted, the API returns SQL Server High Availability states for all SQL Server High Availability instances.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_instance_sql_ha_states_request_max_results_integer.DescribeInstanceSqlHaStatesRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the results. Supported filters include:</p> <ul> <li> <p> <code>tag:<key></code> - The tag key and value pair assigned to the instance. For example, to find all instances tagged with <code>Owner:TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The tag key assigned to the instance.</p> </li> <li> <p> <code>haStatus</code> - The SQL Server High Availability status of the SQL Server High Availability instance (<code>processing</code> | <code>active</code> | <code>standby</code> | <code>invalid</code>).</p> </li> <li> <p> <code>sqlServerLicenseUsage</code> - The license type for the SQL Server license (<code>full</code> | <code>waived</code>).</p> </li> </ul>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceSqlHaStatesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeInstanceSqlHaStatesRequest:
    out: DescribeInstanceSqlHaStatesRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIds") is not None:
        import capo_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceIds"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
