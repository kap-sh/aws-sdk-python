"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainDeliverabilityTrackingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.domain_deliverability_tracking_option

DomainDeliverabilityTrackingOptions: TypeAlias = list[
    "aws_sdk_sesv2.types.domain_deliverability_tracking_option.DomainDeliverabilityTrackingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityTrackingOptions) -> list:
    import aws_sdk_sesv2.types.domain_deliverability_tracking_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sesv2.types.domain_deliverability_tracking_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DomainDeliverabilityTrackingOptions:
    import aws_sdk_sesv2.types.domain_deliverability_tracking_option

    out: DomainDeliverabilityTrackingOptions = []
    for item in data:
        out.append(
            aws_sdk_sesv2.types.domain_deliverability_tracking_option.deserialize_json(
                item
            )
        )
    return out
