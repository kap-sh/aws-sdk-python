"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectAclOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.grants
    import capo_s3.types.owner
    import capo_s3.types.request_charged


class GetObjectAclOutput(TypedDict, closed=True):
    owner: NotRequired["capo_s3.types.owner.Owner"]
    """<p> Container for the bucket owner's ID.</p>"""
    grants: NotRequired["capo_s3.types.grants.Grants"]
    """<p>A list of grants.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: GetObjectAclOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "owner" in value:
        import capo_s3.types.owner

        capo_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "grants" in value:
        import capo_s3.types.grants

        capo_s3.types.grants.serialize_xml(value["grants"], el, "AccessControlList")


def deserialize_xml(el: Element) -> GetObjectAclOutput:
    out: GetObjectAclOutput = {}  # type: ignore[typeddict-item]
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner

        out["owner"] = capo_s3.types.owner.deserialize_xml(child_owner)
    child_grants = el.find("AccessControlList")
    if child_grants is not None:
        import capo_s3.types.grants

        out["grants"] = capo_s3.types.grants.deserialize_xml(child_grants)
    return out
