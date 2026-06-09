"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionNonCompliantResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VpcEncryptionNonCompliantResource(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the non-compliant resource.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of the non-compliant resource.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the non-compliant resource.</p>"""
    is_excludable: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the resource can be excluded from encryption enforcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionNonCompliantResource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "is_excludable" in value:
        pairs.append(
            (f"{prefix}.IsExcludable", "true" if value["is_excludable"] else "false")
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionNonCompliantResource:
    out: VpcEncryptionNonCompliantResource = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_is_excludable = el.find("IsExcludable")
    if child_is_excludable is not None:
        out["is_excludable"] = (child_is_excludable.text or "").lower() == "true"
    return out
