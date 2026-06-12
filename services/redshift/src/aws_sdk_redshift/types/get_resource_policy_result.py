"""Generated from Smithy shape ``com.amazonaws.redshift#GetResourcePolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.resource_policy


class GetResourcePolicyResult(TypedDict):
    resource_policy: NotRequired[
        "aws_sdk_redshift.types.resource_policy.ResourcePolicy"
    ]
    """<p>The content of the resource policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetResourcePolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_policy" in value:
        import aws_sdk_redshift.types.resource_policy

        aws_sdk_redshift.types.resource_policy.serialize_query(
            value["resource_policy"], pairs, f"{prefix}.ResourcePolicy"
        )


def deserialize_query(el: Element) -> GetResourcePolicyResult:
    out: GetResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_resource_policy = el.find("ResourcePolicy")
    if child_resource_policy is not None:
        import aws_sdk_redshift.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_redshift.types.resource_policy.deserialize_query(
                child_resource_policy
            )
        )
    return out
