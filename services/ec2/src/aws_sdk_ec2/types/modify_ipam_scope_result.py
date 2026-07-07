"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamScopeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope


class ModifyIpamScopeResult(TypedDict, closed=True):
    ipam_scope: NotRequired["aws_sdk_ec2.types.ipam_scope.IpamScope"]
    """<p>The results of the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamScopeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_scope" in value:
        import aws_sdk_ec2.types.ipam_scope

        aws_sdk_ec2.types.ipam_scope.serialize_ec2_query(
            value["ipam_scope"], pairs, f"{prefix}.IpamScope"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamScopeResult:
    out: ModifyIpamScopeResult = {}  # type: ignore[typeddict-item]
    child_ipam_scope = el.find("IpamScope")
    if child_ipam_scope is not None:
        import aws_sdk_ec2.types.ipam_scope

        out["ipam_scope"] = aws_sdk_ec2.types.ipam_scope.deserialize_ec2_query(
            child_ipam_scope
        )
    return out
