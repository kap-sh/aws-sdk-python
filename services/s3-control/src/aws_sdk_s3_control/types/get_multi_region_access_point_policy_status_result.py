"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointPolicyStatusResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.policy_status


class GetMultiRegionAccessPointPolicyStatusResult(TypedDict):
    established: NotRequired["aws_sdk_s3_control.types.policy_status.PolicyStatus"]


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointPolicyStatusResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "established" in value:
        import aws_sdk_s3_control.types.policy_status

        aws_sdk_s3_control.types.policy_status.serialize_xml(
            value["established"], el, "Established"
        )


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointPolicyStatusResult:
    out: GetMultiRegionAccessPointPolicyStatusResult = {}  # type: ignore[typeddict-item]
    child_established = el.find("Established")
    if child_established is not None:
        import aws_sdk_s3_control.types.policy_status

        out["established"] = aws_sdk_s3_control.types.policy_status.deserialize_xml(
            child_established
        )
    return out
