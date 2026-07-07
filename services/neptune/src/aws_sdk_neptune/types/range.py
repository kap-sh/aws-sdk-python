"""Generated from Smithy shape ``com.amazonaws.neptune#Range``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.integer
    import aws_sdk_neptune.types.integer_optional

Range = TypedDict(
    "Range",
    {
        "from": NotRequired["aws_sdk_neptune.types.integer.Integer"],
        "to": NotRequired["aws_sdk_neptune.types.integer.Integer"],
        "step": NotRequired["aws_sdk_neptune.types.integer_optional.IntegerOptional"],
    },
    closed=True,
)


# --- awsQuery ser/de ---
def serialize_query(value: Range, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "from" in value:
        pairs.append((f"{prefix}.From", str(value["from"])))
    if "to" in value:
        pairs.append((f"{prefix}.To", str(value["to"])))
    if "step" in value:
        pairs.append((f"{prefix}.Step", str(value["step"])))


def deserialize_query(el: Element) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    child_from = el.find("From")
    if child_from is not None:
        out["from"] = int(child_from.text or "")
    child_to = el.find("To")
    if child_to is not None:
        out["to"] = int(child_to.text or "")
    child_step = el.find("Step")
    if child_step is not None:
        out["step"] = int(child_step.text or "")
    return out
