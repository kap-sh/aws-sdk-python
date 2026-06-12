"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_policy_document


class GetMultiRegionAccessPointPolicyResult(TypedDict):
    policy: NotRequired[
        "aws_sdk_s3_control.types.multi_region_access_point_policy_document.MultiRegionAccessPointPolicyDocument"
    ]
    """<p>The policy associated with the specified Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointPolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        import aws_sdk_s3_control.types.multi_region_access_point_policy_document

        aws_sdk_s3_control.types.multi_region_access_point_policy_document.serialize_xml(
            value["policy"], el, "Policy"
        )


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointPolicyResult:
    out: GetMultiRegionAccessPointPolicyResult = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        import aws_sdk_s3_control.types.multi_region_access_point_policy_document

        out["policy"] = (
            aws_sdk_s3_control.types.multi_region_access_point_policy_document.deserialize_xml(
                child_policy
            )
        )
    return out
