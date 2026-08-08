"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamScopeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_scope


class CreateIpamScopeResult(TypedDict, closed=True):
    ipam_scope: NotRequired["capo_ec2.types.ipam_scope.IpamScope"]
    """<p>Information about the created scope.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamScopeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_scope" in value:
        import capo_ec2.types.ipam_scope

        capo_ec2.types.ipam_scope.serialize_ec2_query(
            value["ipam_scope"], pairs, f"{key_prefix}IpamScope"
        )


def deserialize_ec2_query(el: Element) -> CreateIpamScopeResult:
    out: CreateIpamScopeResult = {}  # type: ignore[typeddict-item]
    child_ipam_scope = el.find("ipamScope")
    if child_ipam_scope is not None:
        import capo_ec2.types.ipam_scope

        out["ipam_scope"] = capo_ec2.types.ipam_scope.deserialize_ec2_query(
            child_ipam_scope
        )
    return out
