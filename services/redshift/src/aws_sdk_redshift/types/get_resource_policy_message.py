"""Generated from Smithy shape ``com.amazonaws.redshift#GetResourcePolicyMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class GetResourcePolicyMessage(TypedDict):
    resource_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource of which its resource policy is fetched.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetResourcePolicyMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> GetResourcePolicyMessage:
    out: GetResourcePolicyMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
