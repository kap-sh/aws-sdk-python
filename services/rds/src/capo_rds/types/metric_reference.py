"""Generated from Smithy shape ``com.amazonaws.rds#MetricReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.reference_details
    import capo_rds.types.string


class MetricReference(TypedDict, closed=True):
    name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the metric reference.</p>"""
    reference_details: NotRequired["capo_rds.types.reference_details.ReferenceDetails"]
    """<p>The details of a performance issue.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricReference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "reference_details" in value:
        import capo_rds.types.reference_details

        capo_rds.types.reference_details.serialize_query(
            value["reference_details"], pairs, f"{key_prefix}ReferenceDetails"
        )


def deserialize_query(el: Element) -> MetricReference:
    out: MetricReference = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_reference_details = el.find("ReferenceDetails")
    if child_reference_details is not None:
        import capo_rds.types.reference_details

        out["reference_details"] = capo_rds.types.reference_details.deserialize_query(
            child_reference_details
        )
    return out
