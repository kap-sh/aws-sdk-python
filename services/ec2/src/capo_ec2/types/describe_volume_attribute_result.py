"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeAttributeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.product_code_list
    import capo_ec2.types.string


class DescribeVolumeAttributeResult(TypedDict, closed=True):
    auto_enable_io: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>The state of <code>autoEnableIO</code> attribute.</p>"""
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>A list of product codes.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVolumeAttributeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_enable_io" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["auto_enable_io"], pairs, f"{key_prefix}AutoEnableIO"
        )
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCodes"
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))


def deserialize_ec2_query(el: Element) -> DescribeVolumeAttributeResult:
    out: DescribeVolumeAttributeResult = {}  # type: ignore[typeddict-item]
    child_auto_enable_io = el.find("AutoEnableIO")
    if child_auto_enable_io is not None:
        import capo_ec2.types.attribute_boolean_value

        out["auto_enable_io"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_auto_enable_io
            )
        )
    if el.find("ProductCodes") is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            el, "ProductCodes"
        )
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    return out
