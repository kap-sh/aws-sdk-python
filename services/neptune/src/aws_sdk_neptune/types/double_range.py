"""Generated from Smithy shape ``com.amazonaws.neptune#DoubleRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.double

DoubleRange = TypedDict(
    "DoubleRange",
    {
        "from": NotRequired["aws_sdk_neptune.types.double.Double"],
        "to": NotRequired["aws_sdk_neptune.types.double.Double"],
    },
    closed=True,
)


# --- awsQuery ser/de ---
def serialize_query(
    value: DoubleRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "from" in value:
        pairs.append((f"{prefix}.From", str(value["from"])))
    if "to" in value:
        pairs.append((f"{prefix}.To", str(value["to"])))


def deserialize_query(el: Element) -> DoubleRange:
    out: DoubleRange = {}  # type: ignore[typeddict-item]
    child_from = el.find("From")
    if child_from is not None:
        out["from"] = float(child_from.text or "")
    child_to = el.find("To")
    if child_to is not None:
        out["to"] = float(child_to.text or "")
    return out
