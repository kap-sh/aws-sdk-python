"""Generated from Smithy shape ``com.amazonaws.cloudformation#ActivateTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.private_type_arn


class ActivateTypeOutput(TypedDict, closed=True):
    arn: NotRequired["capo_cloudformation.types.private_type_arn.PrivateTypeArn"]
    """<p>The Amazon Resource Name (ARN) of the activated extension in this account and Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivateTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))


def deserialize_query(el: Element) -> ActivateTypeOutput:
    out: ActivateTypeOutput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
