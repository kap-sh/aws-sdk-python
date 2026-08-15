"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointPayerResponsibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.payer_responsibility_scope
    import capo_ec2.types.payer_responsibility_type
    import capo_ec2.types.vpc_endpoint_id
    import capo_ec2.types.vpc_endpoint_service_id


class ModifyVpcEndpointPayerResponsibilityRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "capo_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the VPC endpoint service.</p>"""
    vpc_endpoint_id: NotRequired["capo_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of the VPC endpoint.</p>"""
    payer_responsibility: NotRequired[
        "capo_ec2.types.payer_responsibility_type.PayerResponsibilityType"
    ]
    """<p>The Amazon Web Services account to which the usage of VPC endpoint is charged.</p>"""
    scope: NotRequired[
        "capo_ec2.types.payer_responsibility_scope.PayerResponsibilityScope"
    ]
    """<p>The scope of usage/charges for which the billing account is being modified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointPayerResponsibilityRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "vpc_endpoint_id" in value:
        pairs.append((f"{key_prefix}VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "payer_responsibility" in value:
        import capo_ec2.types.payer_responsibility_type

        capo_ec2.types.payer_responsibility_type.serialize_ec2_query(
            value["payer_responsibility"], pairs, f"{key_prefix}PayerResponsibility"
        )
    if "scope" in value:
        import capo_ec2.types.payer_responsibility_scope

        capo_ec2.types.payer_responsibility_scope.serialize_ec2_query(
            value["scope"], pairs, f"{key_prefix}Scope"
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointPayerResponsibilityRequest:
    out: ModifyVpcEndpointPayerResponsibilityRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_payer_responsibility = el.find("PayerResponsibility")
    if child_payer_responsibility is not None:
        import capo_ec2.types.payer_responsibility_type

        out["payer_responsibility"] = (
            capo_ec2.types.payer_responsibility_type.deserialize_ec2_query(
                child_payer_responsibility
            )
        )
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_ec2.types.payer_responsibility_scope

        out["scope"] = capo_ec2.types.payer_responsibility_scope.deserialize_ec2_query(
            child_scope
        )
    return out
