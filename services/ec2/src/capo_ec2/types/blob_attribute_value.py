"""Generated from Smithy shape ``com.amazonaws.ec2#BlobAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.blob


class BlobAttributeValue(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.blob.Blob"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BlobAttributeValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "value" in value:
        import capo_ec2.types.blob

        capo_ec2.types.blob.serialize_ec2_query(
            value["value"], pairs, f"{prefix}.Value"
        )


def deserialize_ec2_query(el: Element) -> BlobAttributeValue:
    out: BlobAttributeValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        import capo_ec2.types.blob

        out["value"] = capo_ec2.types.blob.deserialize_ec2_query(child_value)
    return out
