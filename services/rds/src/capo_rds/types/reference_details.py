"""Generated from Smithy shape ``com.amazonaws.rds#ReferenceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.scalar_reference_details


class ReferenceDetails(TypedDict, closed=True):
    scalar_reference_details: NotRequired[
        "capo_rds.types.scalar_reference_details.ScalarReferenceDetails"
    ]
    """<p>The metric reference details when the reference is a scalar.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReferenceDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scalar_reference_details" in value:
        import capo_rds.types.scalar_reference_details

        capo_rds.types.scalar_reference_details.serialize_query(
            value["scalar_reference_details"],
            pairs,
            f"{key_prefix}ScalarReferenceDetails",
        )


def deserialize_query(el: Element) -> ReferenceDetails:
    out: ReferenceDetails = {}  # type: ignore[typeddict-item]
    child_scalar_reference_details = el.find("ScalarReferenceDetails")
    if child_scalar_reference_details is not None:
        import capo_rds.types.scalar_reference_details

        out["scalar_reference_details"] = (
            capo_rds.types.scalar_reference_details.deserialize_query(
                child_scalar_reference_details
            )
        )
    return out
