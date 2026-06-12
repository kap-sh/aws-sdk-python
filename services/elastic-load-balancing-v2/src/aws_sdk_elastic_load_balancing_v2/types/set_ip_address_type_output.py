"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetIpAddressTypeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.ip_address_type


class SetIpAddressTypeOutput(TypedDict):
    ip_address_type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIpAddressTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ip_address_type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.ip_address_type

        aws_sdk_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )


def deserialize_query(el: Element) -> SetIpAddressTypeOutput:
    out: SetIpAddressTypeOutput = {}  # type: ignore[typeddict-item]
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_elastic_load_balancing_v2.types.ip_address_type.deserialize_query(
                child_ip_address_type
            )
        )
    return out
