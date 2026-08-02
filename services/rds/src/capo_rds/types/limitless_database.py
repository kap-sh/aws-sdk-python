"""Generated from Smithy shape ``com.amazonaws.rds#LimitlessDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.double_optional
    import capo_rds.types.limitless_database_status


class LimitlessDatabase(TypedDict, closed=True):
    status: NotRequired[
        "capo_rds.types.limitless_database_status.LimitlessDatabaseStatus"
    ]
    """<p>The status of Aurora Limitless Database.</p>"""
    min_required_acu: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum required capacity for Aurora Limitless Database in Aurora capacity units (ACUs).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LimitlessDatabase, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_rds.types.limitless_database_status

        capo_rds.types.limitless_database_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "min_required_acu" in value:
        pairs.append((f"{key_prefix}MinRequiredACU", str(value["min_required_acu"])))


def deserialize_query(el: Element) -> LimitlessDatabase:
    out: LimitlessDatabase = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_rds.types.limitless_database_status

        out["status"] = capo_rds.types.limitless_database_status.deserialize_query(
            child_status
        )
    child_min_required_acu = el.find("MinRequiredACU")
    if child_min_required_acu is not None:
        out["min_required_acu"] = float(child_min_required_acu.text or "")
    return out
