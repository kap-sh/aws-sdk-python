"""Generated from Smithy shape ``com.amazonaws.ec2#GetAllowedImagesSettingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_criterion_list
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.string


class GetAllowedImagesSettingsResult(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the Allowed AMIs setting at the account level in the specified Amazon Web Services Region.</p> <p>Possible values:</p> <ul> <li> <p> <code>disabled</code>: All AMIs are allowed.</p> </li> <li> <p> <code>audit-mode</code>: All AMIs are allowed, but the <code>ImageAllowed</code> field is set to <code>true</code> if the AMI would be allowed with the current list of criteria if allowed AMIs was enabled.</p> </li> <li> <p> <code>enabled</code>: Only AMIs matching the image criteria are discoverable and available for use.</p> </li> </ul>"""
    image_criteria: NotRequired[
        "aws_sdk_ec2.types.image_criterion_list.ImageCriterionList"
    ]
    """<p>The list of criteria for images that are discoverable and usable in the account in the specified Amazon Web Services Region.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the Allowed AMIs settings. Possible values include:</p> <ul> <li> <p> <code>account</code> - The Allowed AMIs settings is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The Allowed AMIs settings is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAllowedImagesSettingsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "image_criteria" in value:
        import aws_sdk_ec2.types.image_criterion_list

        aws_sdk_ec2.types.image_criterion_list.serialize_ec2_query(
            value["image_criteria"], pairs, f"{prefix}.ImageCriterionSet"
        )
    if "managed_by" in value:
        import aws_sdk_ec2.types.managed_by

        aws_sdk_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{prefix}.ManagedBy"
        )


def deserialize_ec2_query(el: Element) -> GetAllowedImagesSettingsResult:
    out: GetAllowedImagesSettingsResult = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    if el.find("ImageCriterionSet") is not None:
        import aws_sdk_ec2.types.image_criterion_list

        out["image_criteria"] = (
            aws_sdk_ec2.types.image_criterion_list.deserialize_ec2_query(
                el, "ImageCriterionSet"
            )
        )
    child_managed_by = el.find("ManagedBy")
    if child_managed_by is not None:
        import aws_sdk_ec2.types.managed_by

        out["managed_by"] = aws_sdk_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
