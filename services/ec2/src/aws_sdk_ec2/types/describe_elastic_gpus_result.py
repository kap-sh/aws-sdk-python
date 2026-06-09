"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeElasticGpusResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_set
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeElasticGpusResult(TypedDict):
    elastic_gpu_set: NotRequired["aws_sdk_ec2.types.elastic_gpu_set.ElasticGpuSet"]
    """<p>Information about the Elastic Graphics accelerators.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of items to return. If the total number of items available is more than the value specified in max-items then a Next-Token will be provided in the output that you can use to resume pagination.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeElasticGpusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "elastic_gpu_set" in value:
        import aws_sdk_ec2.types.elastic_gpu_set

        aws_sdk_ec2.types.elastic_gpu_set.serialize_ec2_query(
            value["elastic_gpu_set"], pairs, f"{prefix}.ElasticGpuSet"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeElasticGpusResult:
    out: DescribeElasticGpusResult = {}  # type: ignore[typeddict-item]
    if el.find("ElasticGpuSet") is not None:
        import aws_sdk_ec2.types.elastic_gpu_set

        out["elastic_gpu_set"] = (
            aws_sdk_ec2.types.elastic_gpu_set.deserialize_ec2_query(el, "ElasticGpuSet")
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
