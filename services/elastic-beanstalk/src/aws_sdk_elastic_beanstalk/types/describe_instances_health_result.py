"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeInstancesHealthResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.instance_health_list
    import aws_sdk_elastic_beanstalk.types.next_token
    import aws_sdk_elastic_beanstalk.types.refreshed_at


class DescribeInstancesHealthResult(TypedDict):
    instance_health_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.instance_health_list.InstanceHealthList"
    ]
    """<p>Detailed health information about each instance.</p> <p>The output differs slightly between Linux and Windows environments. There is a difference in the members that are supported under the <code><CPUUtilization></code> type.</p>"""
    refreshed_at: NotRequired[
        "aws_sdk_elastic_beanstalk.types.refreshed_at.RefreshedAt"
    ]
    """<p>The date and time that the health information was retrieved.</p>"""
    next_token: NotRequired["aws_sdk_elastic_beanstalk.types.next_token.NextToken"]
    """<p>Pagination token for the next page of results, if available.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInstancesHealthResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_health_list" in value:
        import aws_sdk_elastic_beanstalk.types.instance_health_list

        aws_sdk_elastic_beanstalk.types.instance_health_list.serialize_query(
            value["instance_health_list"], pairs, f"{prefix}.InstanceHealthList"
        )
    if "refreshed_at" in value:
        import aws_sdk_elastic_beanstalk.types.refreshed_at

        aws_sdk_elastic_beanstalk.types.refreshed_at.serialize_query(
            value["refreshed_at"], pairs, f"{prefix}.RefreshedAt"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeInstancesHealthResult:
    out: DescribeInstancesHealthResult = {}  # type: ignore[typeddict-item]
    child_instance_health_list = el.find("InstanceHealthList")
    if child_instance_health_list is not None:
        import aws_sdk_elastic_beanstalk.types.instance_health_list

        out["instance_health_list"] = (
            aws_sdk_elastic_beanstalk.types.instance_health_list.deserialize_query(
                child_instance_health_list
            )
        )
    child_refreshed_at = el.find("RefreshedAt")
    if child_refreshed_at is not None:
        import aws_sdk_elastic_beanstalk.types.refreshed_at

        out["refreshed_at"] = (
            aws_sdk_elastic_beanstalk.types.refreshed_at.deserialize_query(
                child_refreshed_at
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
