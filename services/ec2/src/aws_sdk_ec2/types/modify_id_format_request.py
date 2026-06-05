"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIdFormatRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ModifyIdFormatRequest(TypedDict):
    resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource: <code>bundle</code> | <code>conversion-task</code> | <code>customer-gateway</code> | <code>dhcp-options</code> | <code>elastic-ip-allocation</code> | <code>elastic-ip-association</code> | <code>export-task</code> | <code>flow-log</code> | <code>image</code> | <code>import-task</code> | <code>internet-gateway</code> | <code>network-acl</code> | <code>network-acl-association</code> | <code>network-interface</code> | <code>network-interface-attachment</code> | <code>prefix-list</code> | <code>route-table</code> | <code>route-table-association</code> | <code>security-group</code> | <code>subnet</code> | <code>subnet-cidr-block-association</code> | <code>vpc</code> | <code>vpc-cidr-block-association</code> | <code>vpc-endpoint</code> | <code>vpc-peering-connection</code> | <code>vpn-connection</code> | <code>vpn-gateway</code>.</p> <p>Alternatively, use the <code>all-current</code> option to include all resource types that are currently within their opt-in period for longer IDs.</p>"""
    use_long_ids: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicate whether the resource should use longer IDs (17-character IDs).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIdFormatRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource" in value:
        pairs.append((f"{prefix}.Resource", str(value["resource"])))
    if "use_long_ids" in value:
        pairs.append(
            (f"{prefix}.UseLongIds", "true" if value["use_long_ids"] else "false")
        )


def deserialize_ec2_query(el: Element) -> ModifyIdFormatRequest:
    out: ModifyIdFormatRequest = {}  # type: ignore[typeddict-item]
    child_resource = el.find("Resource")
    if child_resource is not None:
        out["resource"] = str(child_resource.text or "")
    child_use_long_ids = el.find("UseLongIds")
    if child_use_long_ids is not None:
        out["use_long_ids"] = (child_use_long_ids.text or "").lower() == "true"
    return out
