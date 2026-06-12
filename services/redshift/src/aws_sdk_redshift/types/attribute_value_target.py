"""Generated from Smithy shape ``com.amazonaws.redshift#AttributeValueTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class AttributeValueTarget(TypedDict):
    attribute_value: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The value of the attribute.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttributeValueTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_value" in value:
        pairs.append((f"{prefix}.AttributeValue", str(value["attribute_value"])))


def deserialize_query(el: Element) -> AttributeValueTarget:
    out: AttributeValueTarget = {}  # type: ignore[typeddict-item]
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
