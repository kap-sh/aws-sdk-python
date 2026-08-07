"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeInstancesHealthResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.instance_health_list
    import capo_elastic_beanstalk.types.next_token
    import capo_elastic_beanstalk.types.refreshed_at


class DescribeInstancesHealthResult(TypedDict, closed=True):
    instance_health_list: NotRequired[
        "capo_elastic_beanstalk.types.instance_health_list.InstanceHealthList"
    ]
    """<p>Detailed health information about each instance.</p> <p>The output differs slightly between Linux and Windows environments. There is a difference in the members that are supported under the <code><CPUUtilization></code> type.</p>"""
    refreshed_at: NotRequired["capo_elastic_beanstalk.types.refreshed_at.RefreshedAt"]
    """<p>The date and time that the health information was retrieved.</p>"""
    next_token: NotRequired["capo_elastic_beanstalk.types.next_token.NextToken"]
    """<p>Pagination token for the next page of results, if available.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInstancesHealthResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_health_list" in value:
        import capo_elastic_beanstalk.types.instance_health_list

        capo_elastic_beanstalk.types.instance_health_list.serialize_query(
            value["instance_health_list"], pairs, f"{key_prefix}InstanceHealthList"
        )
    if "refreshed_at" in value:
        import capo_elastic_beanstalk.types.refreshed_at

        capo_elastic_beanstalk.types.refreshed_at.serialize_query(
            value["refreshed_at"], pairs, f"{key_prefix}RefreshedAt"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeInstancesHealthResult:
    out: DescribeInstancesHealthResult = {}  # type: ignore[typeddict-item]
    child_instance_health_list = el.find("InstanceHealthList")
    if child_instance_health_list is not None:
        import capo_elastic_beanstalk.types.instance_health_list

        out["instance_health_list"] = (
            capo_elastic_beanstalk.types.instance_health_list.deserialize_query(
                child_instance_health_list
            )
        )
    child_refreshed_at = el.find("RefreshedAt")
    if child_refreshed_at is not None:
        import capo_elastic_beanstalk.types.refreshed_at

        out["refreshed_at"] = (
            capo_elastic_beanstalk.types.refreshed_at.deserialize_query(
                child_refreshed_at
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
