"""Generated from Smithy shape ``com.amazonaws.rds#Outpost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class Outpost(TypedDict, closed=True):
    arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Outpost, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_query(el: Element) -> Outpost:
    out: Outpost = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
