"""Generated from Smithy shape ``com.amazonaws.cloudformation#PublishTypeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.type_arn


class PublishTypeOutput(TypedDict, closed=True):
    public_type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) assigned to the public extension upon publication.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishTypeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "public_type_arn" in value:
        pairs.append((f"{key_prefix}PublicTypeArn", str(value["public_type_arn"])))


def deserialize_query(el: Element) -> PublishTypeOutput:
    out: PublishTypeOutput = {}  # type: ignore[typeddict-item]
    child_public_type_arn = el.find("PublicTypeArn")
    if child_public_type_arn is not None:
        out["public_type_arn"] = str(child_public_type_arn.text or "")
    return out
