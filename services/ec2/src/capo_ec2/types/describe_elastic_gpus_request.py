"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeElasticGpusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_elastic_gpus_max_results
    import capo_ec2.types.elastic_gpu_id_set
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeElasticGpusRequest(TypedDict, closed=True):
    elastic_gpu_ids: NotRequired["capo_ec2.types.elastic_gpu_id_set.ElasticGpuIdSet"]
    """<p>The Elastic Graphics accelerator IDs.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone in which the Elastic Graphics accelerator resides.</p> </li> <li> <p> <code>elastic-gpu-health</code> - The status of the Elastic Graphics accelerator (<code>OK</code> | <code>IMPAIRED</code>).</p> </li> <li> <p> <code>elastic-gpu-state</code> - The state of the Elastic Graphics accelerator (<code>ATTACHED</code>).</p> </li> <li> <p> <code>elastic-gpu-type</code> - The type of Elastic Graphics accelerator; for example, <code>eg1.medium</code>.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance to which the Elastic Graphics accelerator is associated.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_elastic_gpus_max_results.DescribeElasticGpusMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 5 and 1000.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeElasticGpusRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "elastic_gpu_ids" in value:
        import capo_ec2.types.elastic_gpu_id_set

        capo_ec2.types.elastic_gpu_id_set.serialize_ec2_query(
            value["elastic_gpu_ids"], pairs, f"{key_prefix}ElasticGpuIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeElasticGpusRequest:
    out: DescribeElasticGpusRequest = {}  # type: ignore[typeddict-item]
    if el.find("ElasticGpuIds") is not None:
        import capo_ec2.types.elastic_gpu_id_set

        out["elastic_gpu_ids"] = (
            capo_ec2.types.elastic_gpu_id_set.deserialize_ec2_query(el, "ElasticGpuIds")
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filters")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
