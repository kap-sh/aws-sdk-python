"""Generated from Smithy shape ``com.amazonaws.redshift#ResourcePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class ResourcePolicy(TypedDict):
    resource_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The resources that a policy is attached to.</p>"""
    policy: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The content of a resource policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourcePolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "policy" in value:
        pairs.append((f"{prefix}.Policy", str(value["policy"])))


def deserialize_query(el: Element) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    return out
