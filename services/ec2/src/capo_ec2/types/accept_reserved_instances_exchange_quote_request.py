"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptReservedInstancesExchangeQuoteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.reserved_instance_id_set
    import capo_ec2.types.target_configuration_request_set


class AcceptReservedInstancesExchangeQuoteRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    reserved_instance_ids: NotRequired[
        "capo_ec2.types.reserved_instance_id_set.ReservedInstanceIdSet"
    ]
    """<p>The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or higher value.</p>"""
    target_configurations: NotRequired[
        "capo_ec2.types.target_configuration_request_set.TargetConfigurationRequestSet"
    ]
    """<p>The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptReservedInstancesExchangeQuoteRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "reserved_instance_ids" in value:
        import capo_ec2.types.reserved_instance_id_set

        capo_ec2.types.reserved_instance_id_set.serialize_ec2_query(
            value["reserved_instance_ids"], pairs, f"{key_prefix}ReservedInstanceIds"
        )
    if "target_configurations" in value:
        import capo_ec2.types.target_configuration_request_set

        capo_ec2.types.target_configuration_request_set.serialize_ec2_query(
            value["target_configurations"], pairs, f"{key_prefix}TargetConfigurations"
        )


def deserialize_ec2_query(el: Element) -> AcceptReservedInstancesExchangeQuoteRequest:
    out: AcceptReservedInstancesExchangeQuoteRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("ReservedInstanceIds") is not None:
        import capo_ec2.types.reserved_instance_id_set

        out["reserved_instance_ids"] = (
            capo_ec2.types.reserved_instance_id_set.deserialize_ec2_query(
                el, "ReservedInstanceIds"
            )
        )
    if el.find("TargetConfigurations") is not None:
        import capo_ec2.types.target_configuration_request_set

        out["target_configurations"] = (
            capo_ec2.types.target_configuration_request_set.deserialize_ec2_query(
                el, "TargetConfigurations"
            )
        )
    return out
