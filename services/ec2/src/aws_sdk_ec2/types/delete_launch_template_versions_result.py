"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_launch_template_versions_response_error_set
    import aws_sdk_ec2.types.delete_launch_template_versions_response_success_set


class DeleteLaunchTemplateVersionsResult(TypedDict):
    successfully_deleted_launch_template_versions: NotRequired[
        "aws_sdk_ec2.types.delete_launch_template_versions_response_success_set.DeleteLaunchTemplateVersionsResponseSuccessSet"
    ]
    """<p>Information about the launch template versions that were successfully deleted.</p>"""
    unsuccessfully_deleted_launch_template_versions: NotRequired[
        "aws_sdk_ec2.types.delete_launch_template_versions_response_error_set.DeleteLaunchTemplateVersionsResponseErrorSet"
    ]
    """<p>Information about the launch template versions that could not be deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLaunchTemplateVersionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successfully_deleted_launch_template_versions" in value:
        import aws_sdk_ec2.types.delete_launch_template_versions_response_success_set

        aws_sdk_ec2.types.delete_launch_template_versions_response_success_set.serialize_ec2_query(
            value["successfully_deleted_launch_template_versions"],
            pairs,
            f"{prefix}.SuccessfullyDeletedLaunchTemplateVersionSet",
        )
    if "unsuccessfully_deleted_launch_template_versions" in value:
        import aws_sdk_ec2.types.delete_launch_template_versions_response_error_set

        aws_sdk_ec2.types.delete_launch_template_versions_response_error_set.serialize_ec2_query(
            value["unsuccessfully_deleted_launch_template_versions"],
            pairs,
            f"{prefix}.UnsuccessfullyDeletedLaunchTemplateVersionSet",
        )


def deserialize_ec2_query(el: Element) -> DeleteLaunchTemplateVersionsResult:
    out: DeleteLaunchTemplateVersionsResult = {}  # type: ignore[typeddict-item]
    if el.find("SuccessfullyDeletedLaunchTemplateVersionSet") is not None:
        import aws_sdk_ec2.types.delete_launch_template_versions_response_success_set

        out["successfully_deleted_launch_template_versions"] = (
            aws_sdk_ec2.types.delete_launch_template_versions_response_success_set.deserialize_ec2_query(
                el, "SuccessfullyDeletedLaunchTemplateVersionSet"
            )
        )
    if el.find("UnsuccessfullyDeletedLaunchTemplateVersionSet") is not None:
        import aws_sdk_ec2.types.delete_launch_template_versions_response_error_set

        out["unsuccessfully_deleted_launch_template_versions"] = (
            aws_sdk_ec2.types.delete_launch_template_versions_response_error_set.deserialize_ec2_query(
                el, "UnsuccessfullyDeletedLaunchTemplateVersionSet"
            )
        )
    return out
