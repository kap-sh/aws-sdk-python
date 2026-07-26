"""Generated from Smithy shape ``com.amazonaws.ec2#GetFlowLogsIntegrationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integrate_services
    import capo_ec2.types.string
    import capo_ec2.types.vpc_flow_log_id


class GetFlowLogsIntegrationTemplateRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    flow_log_id: NotRequired["capo_ec2.types.vpc_flow_log_id.VpcFlowLogId"]
    """<p>The ID of the flow log.</p>"""
    config_delivery_s3_destination_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>To store the CloudFormation template in Amazon S3, specify the location in Amazon S3.</p>"""
    integrate_services: NotRequired[
        "capo_ec2.types.integrate_services.IntegrateServices"
    ]
    """<p>Information about the service integration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetFlowLogsIntegrationTemplateRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "flow_log_id" in value:
        pairs.append((f"{prefix}.FlowLogId", str(value["flow_log_id"])))
    if "config_delivery_s3_destination_arn" in value:
        pairs.append(
            (
                f"{prefix}.ConfigDeliveryS3DestinationArn",
                str(value["config_delivery_s3_destination_arn"]),
            )
        )
    if "integrate_services" in value:
        import capo_ec2.types.integrate_services

        capo_ec2.types.integrate_services.serialize_ec2_query(
            value["integrate_services"], pairs, f"{prefix}.IntegrateServices"
        )


def deserialize_ec2_query(el: Element) -> GetFlowLogsIntegrationTemplateRequest:
    out: GetFlowLogsIntegrationTemplateRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_flow_log_id = el.find("FlowLogId")
    if child_flow_log_id is not None:
        out["flow_log_id"] = str(child_flow_log_id.text or "")
    child_config_delivery_s3_destination_arn = el.find("ConfigDeliveryS3DestinationArn")
    if child_config_delivery_s3_destination_arn is not None:
        out["config_delivery_s3_destination_arn"] = str(
            child_config_delivery_s3_destination_arn.text or ""
        )
    child_integrate_services = el.find("IntegrateServices")
    if child_integrate_services is not None:
        import capo_ec2.types.integrate_services

        out["integrate_services"] = (
            capo_ec2.types.integrate_services.deserialize_ec2_query(
                child_integrate_services
            )
        )
    return out
