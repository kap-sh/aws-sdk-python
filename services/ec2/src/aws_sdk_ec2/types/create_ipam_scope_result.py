"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamScopeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope


class CreateIpamScopeResult(TypedDict):
    ipam_scope: NotRequired["aws_sdk_ec2.types.ipam_scope.IpamScope"]
    """<p>Information about the created scope.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamScopeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_scope" in value:
        import aws_sdk_ec2.types.ipam_scope

        aws_sdk_ec2.types.ipam_scope.serialize_ec2_query(
            value["ipam_scope"], pairs, f"{prefix}.IpamScope"
        )


def deserialize_ec2_query(el: Element) -> CreateIpamScopeResult:
    out: CreateIpamScopeResult = {}  # type: ignore[typeddict-item]
    child_ipam_scope = el.find("IpamScope")
    if child_ipam_scope is not None:
        import aws_sdk_ec2.types.ipam_scope

        out["ipam_scope"] = aws_sdk_ec2.types.ipam_scope.deserialize_ec2_query(
            child_ipam_scope
        )
    return out
