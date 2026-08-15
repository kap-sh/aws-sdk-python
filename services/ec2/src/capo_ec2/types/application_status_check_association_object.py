"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusCheckAssociationObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_id
    import capo_ec2.types.association_type_enum
    import capo_ec2.types.string


class ApplicationStatusCheckAssociationObject(TypedDict, closed=True):
    application_status_check_id: NotRequired[
        "capo_ec2.types.application_status_check_id.ApplicationStatusCheckId"
    ]
    """<p>The ID of the application status check.</p>"""
    association_type: NotRequired[
        "capo_ec2.types.association_type_enum.AssociationTypeEnum"
    ]
    """<p>The type of target that the application status check is associated with. Possible values:</p> <ul> <li> <p> <code>tag</code> – The check applies to current and future instances with a matching tag key-value pair.</p> </li> <li> <p> <code>instance-id</code> – The check applies to a specific instance.</p> </li> </ul>"""
    key: NotRequired["capo_ec2.types.string.String"]
    """<p>The key for the association. This value is present only for tag-based associations, where it contains the tag key. For instance-based associations, this value is absent.</p>"""
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The value for the association target. For tag-based associations, this is the tag value. For instance-based associations, this is the instance ID (for example, <code>i-0123456789abcdef0</code>).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatusCheckAssociationObject,
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
        import capo_ec2.types.association_type_enum

        capo_ec2.types.association_type_enum.serialize_ec2_query(
            value["association_type"], pairs, f"{key_prefix}AssociationType"
        )
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> ApplicationStatusCheckAssociationObject:
    out: ApplicationStatusCheckAssociationObject = {}  # type: ignore[typeddict-item]
    child_application_status_check_id = el.find("applicationStatusCheckId")
    if child_application_status_check_id is not None:
        out["application_status_check_id"] = str(
            child_application_status_check_id.text or ""
        )
    child_association_type = el.find("associationType")
    if child_association_type is not None:
        import capo_ec2.types.association_type_enum

        out["association_type"] = (
            capo_ec2.types.association_type_enum.deserialize_ec2_query(
                child_association_type
            )
        )
    child_key = el.find("key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_value = el.find("value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
