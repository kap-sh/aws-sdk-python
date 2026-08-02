"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceImageCriteriaInAllowedImagesSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_criterion_request_list


class ReplaceImageCriteriaInAllowedImagesSettingsRequest(TypedDict, closed=True):
    image_criteria: NotRequired[
        "capo_ec2.types.image_criterion_request_list.ImageCriterionRequestList"
    ]
    """<p>The list of criteria that are evaluated to determine whether AMIs are discoverable and usable in the account in the specified Amazon Web Services Region.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceImageCriteriaInAllowedImagesSettingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_criteria" in value:
        import capo_ec2.types.image_criterion_request_list

        capo_ec2.types.image_criterion_request_list.serialize_ec2_query(
            value["image_criteria"], pairs, f"{key_prefix}ImageCriteria"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ReplaceImageCriteriaInAllowedImagesSettingsRequest:
    out: ReplaceImageCriteriaInAllowedImagesSettingsRequest = {}  # type: ignore[typeddict-item]
    if el.find("ImageCriteria") is not None:
        import capo_ec2.types.image_criterion_request_list

        out["image_criteria"] = (
            capo_ec2.types.image_criterion_request_list.deserialize_ec2_query(
                el, "ImageCriteria"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
