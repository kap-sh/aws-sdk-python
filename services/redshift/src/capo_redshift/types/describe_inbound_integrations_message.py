"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeInboundIntegrationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.inbound_integration_arn
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string
    import capo_redshift.types.target_arn


class DescribeInboundIntegrationsMessage(TypedDict, closed=True):
    integration_arn: NotRequired[
        "capo_redshift.types.inbound_integration_arn.InboundIntegrationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inbound integration.</p>"""
    target_arn: NotRequired["capo_redshift.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the target of an inbound integration.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeInboundIntegrations</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInboundIntegrationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_arn" in value:
        pairs.append((f"{prefix}.IntegrationArn", str(value["integration_arn"])))
    if "target_arn" in value:
        pairs.append((f"{prefix}.TargetArn", str(value["target_arn"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeInboundIntegrationsMessage:
    out: DescribeInboundIntegrationsMessage = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
