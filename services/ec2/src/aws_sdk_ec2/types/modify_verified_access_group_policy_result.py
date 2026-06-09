"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_sse_specification_response


class ModifyVerifiedAccessGroupPolicyResult(TypedDict):
    policy_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessGroupPolicyResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "policy_enabled" in value:
        pairs.append(
            (f"{prefix}.PolicyEnabled", "true" if value["policy_enabled"] else "false")
        )
    if "policy_document" in value:
        pairs.append((f"{prefix}.PolicyDocument", str(value["policy_document"])))
    if "sse_specification" in value:
        import aws_sdk_ec2.types.verified_access_sse_specification_response

        aws_sdk_ec2.types.verified_access_sse_specification_response.serialize_ec2_query(
            value["sse_specification"], pairs, f"{prefix}.SseSpecification"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessGroupPolicyResult:
    out: ModifyVerifiedAccessGroupPolicyResult = {}  # type: ignore[typeddict-item]
    child_policy_enabled = el.find("PolicyEnabled")
    if child_policy_enabled is not None:
        out["policy_enabled"] = (child_policy_enabled.text or "").lower() == "true"
    child_policy_document = el.find("PolicyDocument")
    if child_policy_document is not None:
        out["policy_document"] = str(child_policy_document.text or "")
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import aws_sdk_ec2.types.verified_access_sse_specification_response

        out["sse_specification"] = (
            aws_sdk_ec2.types.verified_access_sse_specification_response.deserialize_ec2_query(
                child_sse_specification
            )
        )
    return out
