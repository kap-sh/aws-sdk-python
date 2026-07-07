"""Generated from Smithy shape ``com.amazonaws.redshift#PutResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.resource_policy


class PutResourcePolicyResult(TypedDict, closed=True):
    resource_policy: NotRequired[
        "aws_sdk_redshift.types.resource_policy.ResourcePolicy"
    ]
    """<p>The content of the updated resource policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutResourcePolicyResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_policy" in value:
        import aws_sdk_redshift.types.resource_policy

        aws_sdk_redshift.types.resource_policy.serialize_query(
            value["resource_policy"], pairs, f"{prefix}.ResourcePolicy"
        )


def deserialize_query(el: Element) -> PutResourcePolicyResult:
    out: PutResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_resource_policy = el.find("ResourcePolicy")
    if child_resource_policy is not None:
        import aws_sdk_redshift.types.resource_policy

        out["resource_policy"] = (
            aws_sdk_redshift.types.resource_policy.deserialize_query(
                child_resource_policy
            )
        )
    return out
