"""Generated from Smithy shape ``com.amazonaws.rds#ScalarReferenceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.double


class ScalarReferenceDetails(TypedDict, closed=True):
    value: NotRequired["capo_rds.types.double.Double"]
    """<p>The value of a scalar reference.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalarReferenceDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> ScalarReferenceDetails:
    out: ScalarReferenceDetails = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = float(child_value.text or "")
    return out
