"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#UpdateRoutingControlStateEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.update_routing_control_state_entry

UpdateRoutingControlStateEntries: TypeAlias = list[
    "capo_route53_recovery_cluster.types.update_routing_control_state_entry.UpdateRoutingControlStateEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRoutingControlStateEntries) -> list:
    import capo_route53_recovery_cluster.types.update_routing_control_state_entry

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_cluster.types.update_routing_control_state_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UpdateRoutingControlStateEntries:
    import capo_route53_recovery_cluster.types.update_routing_control_state_entry

    out: UpdateRoutingControlStateEntries = []
    for item in data:
        out.append(
            capo_route53_recovery_cluster.types.update_routing_control_state_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
