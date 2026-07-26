"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.byoip_cidr_event

ByoipCidrEvents: TypeAlias = list[
    "capo_global_accelerator.types.byoip_cidr_event.ByoipCidrEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidrEvents) -> list:
    import capo_global_accelerator.types.byoip_cidr_event

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.byoip_cidr_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ByoipCidrEvents:
    import capo_global_accelerator.types.byoip_cidr_event

    out: ByoipCidrEvents = []
    for item in data:
        out.append(
            capo_global_accelerator.types.byoip_cidr_event.deserialize_aws_json_1_1(
                item
            )
        )
    return out
