"""Generated from Smithy shape ``com.amazonaws.rds#DoubleRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.double

DoubleRange = TypedDict(
    "DoubleRange",
    {
        "from": NotRequired["capo_rds.types.double.Double"],
        "to": NotRequired["capo_rds.types.double.Double"],
    },
    closed=True,
)


# --- awsQuery ser/de ---
def serialize_query(
    value: DoubleRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from" in value:
        pairs.append(
            (
                f"{key_prefix}From",
                (
                    "NaN"
                    if value["from"] != value["from"]
                    else "Infinity"
                    if value["from"] == float("inf")
                    else "-Infinity"
                    if value["from"] == float("-inf")
                    else str(value["from"])
                ),
            )
        )
    if "to" in value:
        pairs.append(
            (
                f"{key_prefix}To",
                (
                    "NaN"
                    if value["to"] != value["to"]
                    else "Infinity"
                    if value["to"] == float("inf")
                    else "-Infinity"
                    if value["to"] == float("-inf")
                    else str(value["to"])
                ),
            )
        )


def deserialize_query(el: Element) -> DoubleRange:
    out: DoubleRange = {}  # type: ignore[typeddict-item]
    child_from = el.find("From")
    if child_from is not None:
        out["from"] = float(child_from.text or "")
    child_to = el.find("To")
    if child_to is not None:
        out["to"] = float(child_to.text or "")
    return out
