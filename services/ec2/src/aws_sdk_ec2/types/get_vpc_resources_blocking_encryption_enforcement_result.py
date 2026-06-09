"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpcResourcesBlockingEncryptionEnforcementResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list


class GetVpcResourcesBlockingEncryptionEnforcementResult(TypedDict):
    non_compliant_resources: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list.VpcEncryptionNonCompliantResourceList"
    ]
    """<p>Information about resources that are blocking encryption enforcement.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpcResourcesBlockingEncryptionEnforcementResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "non_compliant_resources" in value:
        import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list

        aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list.serialize_ec2_query(
            value["non_compliant_resources"], pairs, f"{prefix}.NonCompliantResourceSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> GetVpcResourcesBlockingEncryptionEnforcementResult:
    out: GetVpcResourcesBlockingEncryptionEnforcementResult = {}  # type: ignore[typeddict-item]
    if el.find("NonCompliantResourceSet") is not None:
        import aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list

        out["non_compliant_resources"] = (
            aws_sdk_ec2.types.vpc_encryption_non_compliant_resource_list.deserialize_ec2_query(
                el, "NonCompliantResourceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
