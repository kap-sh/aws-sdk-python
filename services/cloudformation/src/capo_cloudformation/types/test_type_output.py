"""Generated from Smithy shape ``com.amazonaws.cloudformation#TestTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_arn


class TestTypeOutput(TypedDict, closed=True):
    type_version_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type_version_arn" in value:
        pairs.append((f"{key_prefix}TypeVersionArn", str(value["type_version_arn"])))


def deserialize_query(el: Element) -> TestTypeOutput:
    out: TestTypeOutput = {}  # type: ignore[typeddict-item]
    child_type_version_arn = el.find("TypeVersionArn")
    if child_type_version_arn is not None:
        out["type_version_arn"] = str(child_type_version_arn.text or "")
    return out
