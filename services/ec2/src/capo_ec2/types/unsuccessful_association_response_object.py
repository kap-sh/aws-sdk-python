"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulAssociationResponseObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_id
    import capo_ec2.types.string


class UnsuccessfulAssociationResponseObject(TypedDict, closed=True):
    application_status_check_id: NotRequired[
        "capo_ec2.types.application_status_check_id.ApplicationStatusCheckId"
    ]
    """<p>The ID of the application status check.</p>"""
    association_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of association. Valid values: <code>EC2TAG</code> and <code>INSTANCE_ID</code>.</p>"""
    association_value: NotRequired["capo_ec2.types.string.String"]
    """<p>The association value. For <code>EC2TAG</code>, the value is formatted as <code>key=value</code>. For <code>INSTANCE_ID</code>, the value is the instance ID.</p>"""
    reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason the association failed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulAssociationResponseObject,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check_id" in value:
        pairs.append(
            (
                f"{key_prefix}ApplicationStatusCheckId",
                str(value["application_status_check_id"]),
            )
        )
    if "association_type" in value:
        pairs.append((f"{key_prefix}AssociationType", str(value["association_type"])))
    if "association_value" in value:
        pairs.append((f"{key_prefix}AssociationValue", str(value["association_value"])))
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))


def deserialize_ec2_query(el: Element) -> UnsuccessfulAssociationResponseObject:
    out: UnsuccessfulAssociationResponseObject = {}  # type: ignore[typeddict-item]
    child_application_status_check_id = el.find("applicationStatusCheckId")
    if child_application_status_check_id is not None:
        out["application_status_check_id"] = str(
            child_application_status_check_id.text or ""
        )
    child_association_type = el.find("associationType")
    if child_association_type is not None:
        out["association_type"] = str(child_association_type.text or "")
    child_association_value = el.find("associationValue")
    if child_association_value is not None:
        out["association_value"] = str(child_association_value.text or "")
    child_reason = el.find("reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
