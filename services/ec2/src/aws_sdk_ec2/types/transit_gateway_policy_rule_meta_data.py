"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyRuleMetaData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class TransitGatewayPolicyRuleMetaData(TypedDict, closed=True):
    meta_data_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key name for the transit gateway policy rule meta data tag.</p>"""
    meta_data_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the key for the transit gateway policy rule meta data tag.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyRuleMetaData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "meta_data_key" in value:
        pairs.append((f"{prefix}.MetaDataKey", str(value["meta_data_key"])))
    if "meta_data_value" in value:
        pairs.append((f"{prefix}.MetaDataValue", str(value["meta_data_value"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyRuleMetaData:
    out: TransitGatewayPolicyRuleMetaData = {}  # type: ignore[typeddict-item]
    child_meta_data_key = el.find("MetaDataKey")
    if child_meta_data_key is not None:
        out["meta_data_key"] = str(child_meta_data_key.text or "")
    child_meta_data_value = el.find("MetaDataValue")
    if child_meta_data_value is not None:
        out["meta_data_value"] = str(child_meta_data_value.text or "")
    return out
