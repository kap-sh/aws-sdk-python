"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AnalysisComponent(TypedDict, closed=True):
    id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the component.</p>"""
    arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the analysis component.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisComponent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> AnalysisComponent:
    out: AnalysisComponent = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
