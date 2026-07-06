"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyIpPoolsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.ipam_pools


class ModifyIpPoolsOutput(TypedDict, closed=True):
    ipam_pools: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.ipam_pools.IpamPools"
    ]
    """<p>The IPAM pool ID.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyIpPoolsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pools" in value:
        import aws_sdk_elastic_load_balancing_v2.types.ipam_pools

        aws_sdk_elastic_load_balancing_v2.types.ipam_pools.serialize_query(
            value["ipam_pools"], pairs, f"{prefix}.IpamPools"
        )


def deserialize_query(el: Element) -> ModifyIpPoolsOutput:
    out: ModifyIpPoolsOutput = {}  # type: ignore[typeddict-item]
    child_ipam_pools = el.find("IpamPools")
    if child_ipam_pools is not None:
        import aws_sdk_elastic_load_balancing_v2.types.ipam_pools

        out["ipam_pools"] = (
            aws_sdk_elastic_load_balancing_v2.types.ipam_pools.deserialize_query(
                child_ipam_pools
            )
        )
    return out
