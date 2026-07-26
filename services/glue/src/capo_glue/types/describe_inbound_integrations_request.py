"""Generated from Smithy shape ``com.amazonaws.glue#DescribeInboundIntegrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.integration_integer
    import capo_glue.types.string128
    import capo_glue.types.string512


class DescribeInboundIntegrationsRequest(TypedDict, closed=True):
    integration_arn: NotRequired["capo_glue.types.string128.String128"]
    """<p>The Amazon Resource Name (ARN) of the integration.</p>"""
    marker: NotRequired["capo_glue.types.string128.String128"]
    """<p>A token to specify where to start paginating. This is the marker from a previously truncated response.</p>"""
    max_records: NotRequired["capo_glue.types.integration_integer.IntegrationInteger"]
    """<p>The total number of items to return in the output.</p>"""
    target_arn: NotRequired["capo_glue.types.string512.String512"]
    """<p>The Amazon Resource Name (ARN) of the target resource in the integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInboundIntegrationsRequest) -> dict:
    out: dict = {}
    if "integration_arn" in value:
        out["IntegrationArn"] = value["integration_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInboundIntegrationsRequest:
    out: DescribeInboundIntegrationsRequest = {}  # type: ignore[typeddict-item]
    if "IntegrationArn" in data:
        out["integration_arn"] = data["IntegrationArn"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    return out
