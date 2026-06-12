"""Generated from Smithy shape ``com.amazonaws.sts#PolicyDescriptorType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.arn_type


class PolicyDescriptorType(TypedDict):
    arn: NotRequired["aws_sdk_sts.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy for the role. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDescriptorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.arn", str(value["arn"])))


def deserialize_query(el: Element) -> PolicyDescriptorType:
    out: PolicyDescriptorType = {}  # type: ignore[typeddict-item]
    child_arn = el.find("arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
