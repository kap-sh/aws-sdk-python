"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.fpga_image_state
    import capo_ec2.types.instance_types_list
    import capo_ec2.types.pci_id
    import capo_ec2.types.product_code_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class FpgaImage(TypedDict, closed=True):
    fpga_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The FPGA image identifier (AFI ID).</p>"""
    fpga_image_global_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The global FPGA image identifier (AGFI ID).</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the AFI.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the AFI.</p>"""
    shell_version: NotRequired["capo_ec2.types.string.String"]
    """<p>The version of the Amazon Web Services Shell that was used to create the bitstream.</p>"""
    pci_id: NotRequired["capo_ec2.types.pci_id.PciId"]
    """<p>Information about the PCI bus.</p>"""
    state: NotRequired["capo_ec2.types.fpga_image_state.FpgaImageState"]
    """<p>Information about the state of the AFI.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time the AFI was created.</p>"""
    update_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time of the most recent update to the AFI.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the AFI.</p>"""
    owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The alias of the AFI owner. Possible values include <code>self</code>, <code>amazon</code>, and <code>aws-marketplace</code>.</p>"""
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes for the AFI.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the AFI.</p>"""
    public: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AFI is public.</p>"""
    data_retention_support: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether data retention support is enabled for the AFI.</p>"""
    instance_types: NotRequired["capo_ec2.types.instance_types_list.InstanceTypesList"]
    """<p>The instance types supported by the AFI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FpgaImage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "fpga_image_id" in value:
        pairs.append((f"{key_prefix}FpgaImageId", str(value["fpga_image_id"])))
    if "fpga_image_global_id" in value:
        pairs.append(
            (f"{key_prefix}FpgaImageGlobalId", str(value["fpga_image_global_id"]))
        )
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "shell_version" in value:
        pairs.append((f"{key_prefix}ShellVersion", str(value["shell_version"])))
    if "pci_id" in value:
        import capo_ec2.types.pci_id

        capo_ec2.types.pci_id.serialize_ec2_query(
            value["pci_id"], pairs, f"{key_prefix}PciId"
        )
    if "state" in value:
        import capo_ec2.types.fpga_image_state

        capo_ec2.types.fpga_image_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "update_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["update_time"], pairs, f"{key_prefix}UpdateTime"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "owner_alias" in value:
        pairs.append((f"{key_prefix}OwnerAlias", str(value["owner_alias"])))
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCodes"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "public" in value:
        pairs.append((f"{key_prefix}Public", "true" if value["public"] else "false"))
    if "data_retention_support" in value:
        pairs.append(
            (
                f"{key_prefix}DataRetentionSupport",
                "true" if value["data_retention_support"] else "false",
            )
        )
    if "instance_types" in value:
        import capo_ec2.types.instance_types_list

        capo_ec2.types.instance_types_list.serialize_ec2_query(
            value["instance_types"], pairs, f"{key_prefix}InstanceTypes"
        )


def deserialize_ec2_query(el: Element) -> FpgaImage:
    out: FpgaImage = {}  # type: ignore[typeddict-item]
    child_fpga_image_id = el.find("FpgaImageId")
    if child_fpga_image_id is not None:
        out["fpga_image_id"] = str(child_fpga_image_id.text or "")
    child_fpga_image_global_id = el.find("FpgaImageGlobalId")
    if child_fpga_image_global_id is not None:
        out["fpga_image_global_id"] = str(child_fpga_image_global_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_shell_version = el.find("ShellVersion")
    if child_shell_version is not None:
        out["shell_version"] = str(child_shell_version.text or "")
    child_pci_id = el.find("PciId")
    if child_pci_id is not None:
        import capo_ec2.types.pci_id

        out["pci_id"] = capo_ec2.types.pci_id.deserialize_ec2_query(child_pci_id)
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.fpga_image_state

        out["state"] = capo_ec2.types.fpga_image_state.deserialize_ec2_query(
            child_state
        )
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_update_time = el.find("UpdateTime")
    if child_update_time is not None:
        import capo_ec2.types.date_time

        out["update_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_update_time
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_owner_alias = el.find("OwnerAlias")
    if child_owner_alias is not None:
        out["owner_alias"] = str(child_owner_alias.text or "")
    if el.find("ProductCodes") is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            el, "ProductCodes"
        )
    if el.find("Tags") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "Tags")
    child_public = el.find("Public")
    if child_public is not None:
        out["public"] = (child_public.text or "").lower() == "true"
    child_data_retention_support = el.find("DataRetentionSupport")
    if child_data_retention_support is not None:
        out["data_retention_support"] = (
            child_data_retention_support.text or ""
        ).lower() == "true"
    if el.find("InstanceTypes") is not None:
        import capo_ec2.types.instance_types_list

        out["instance_types"] = (
            capo_ec2.types.instance_types_list.deserialize_ec2_query(
                el, "InstanceTypes"
            )
        )
    return out
