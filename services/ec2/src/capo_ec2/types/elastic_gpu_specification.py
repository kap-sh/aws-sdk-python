"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ElasticGpuSpecification(TypedDict, closed=True):
    type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of Elastic Graphics accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ElasticGpuSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))


def deserialize_ec2_query(el: Element) -> ElasticGpuSpecification:
    out: ElasticGpuSpecification = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    return out
