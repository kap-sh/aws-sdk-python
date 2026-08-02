"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotAttributeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_volume_permission_list
    import capo_ec2.types.product_code_list
    import capo_ec2.types.string


class DescribeSnapshotAttributeResult(TypedDict, closed=True):
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the EBS snapshot.</p>"""
    create_volume_permissions: NotRequired[
        "capo_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>The users and groups that have the permissions for creating volumes from the snapshot.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSnapshotAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCodes"
        )
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "create_volume_permissions" in value:
        import capo_ec2.types.create_volume_permission_list

        capo_ec2.types.create_volume_permission_list.serialize_ec2_query(
            value["create_volume_permissions"],
            pairs,
            f"{key_prefix}CreateVolumePermission",
        )


def deserialize_ec2_query(el: Element) -> DescribeSnapshotAttributeResult:
    out: DescribeSnapshotAttributeResult = {}  # type: ignore[typeddict-item]
    if el.find("ProductCodes") is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            el, "ProductCodes"
        )
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    if el.find("CreateVolumePermission") is not None:
        import capo_ec2.types.create_volume_permission_list

        out["create_volume_permissions"] = (
            capo_ec2.types.create_volume_permission_list.deserialize_ec2_query(
                el, "CreateVolumePermission"
            )
        )
    return out
