"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AvailabilityOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.multi_az
    import capo_cloudsearch.types.option_status


class AvailabilityOptionsStatus(TypedDict, closed=True):
    options: "capo_cloudsearch.types.multi_az.MultiAZ"
    """<p>The availability options configured for the domain.</p>"""
    status: "capo_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityOptionsStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}Options", "true" if value.get("options", False) else "false")
    )
    import capo_cloudsearch.types.option_status

    capo_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> AvailabilityOptionsStatus:
    out: AvailabilityOptionsStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        out["options"] = (child_options.text or "").lower() == "true"
    else:
        out["options"] = False
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudsearch.types.option_status

        out["status"] = capo_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("AvailabilityOptionsStatus.status required")
    return out
