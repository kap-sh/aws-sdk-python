"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointPolicyDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.established_multi_region_access_point_policy
    import aws_sdk_s3_control.types.proposed_multi_region_access_point_policy


class MultiRegionAccessPointPolicyDocument(TypedDict):
    established: NotRequired[
        "aws_sdk_s3_control.types.established_multi_region_access_point_policy.EstablishedMultiRegionAccessPointPolicy"
    ]
    """<p>The last established policy for the Multi-Region Access Point.</p>"""
    proposed: NotRequired[
        "aws_sdk_s3_control.types.proposed_multi_region_access_point_policy.ProposedMultiRegionAccessPointPolicy"
    ]
    """<p>The proposed policy for the Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointPolicyDocument, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "established" in value:
        import aws_sdk_s3_control.types.established_multi_region_access_point_policy

        aws_sdk_s3_control.types.established_multi_region_access_point_policy.serialize_xml(
            value["established"], el, "Established"
        )
    if "proposed" in value:
        import aws_sdk_s3_control.types.proposed_multi_region_access_point_policy

        aws_sdk_s3_control.types.proposed_multi_region_access_point_policy.serialize_xml(
            value["proposed"], el, "Proposed"
        )


def deserialize_xml(el: Element) -> MultiRegionAccessPointPolicyDocument:
    out: MultiRegionAccessPointPolicyDocument = {}  # type: ignore[typeddict-item]
    child_established = el.find("Established")
    if child_established is not None:
        import aws_sdk_s3_control.types.established_multi_region_access_point_policy

        out["established"] = (
            aws_sdk_s3_control.types.established_multi_region_access_point_policy.deserialize_xml(
                child_established
            )
        )
    child_proposed = el.find("Proposed")
    if child_proposed is not None:
        import aws_sdk_s3_control.types.proposed_multi_region_access_point_policy

        out["proposed"] = (
            aws_sdk_s3_control.types.proposed_multi_region_access_point_policy.deserialize_xml(
                child_proposed
            )
        )
    return out
