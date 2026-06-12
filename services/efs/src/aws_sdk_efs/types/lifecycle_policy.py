"""Generated from Smithy shape ``com.amazonaws.efs#LifecyclePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.transition_to_archive_rules
    import aws_sdk_efs.types.transition_to_ia_rules
    import aws_sdk_efs.types.transition_to_primary_storage_class_rules


class LifecyclePolicy(TypedDict):
    transition_to_ia: NotRequired[
        "aws_sdk_efs.types.transition_to_ia_rules.TransitionToIARules"
    ]
    """<p>The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory don't count as file access events.</p>"""
    transition_to_primary_storage_class: NotRequired[
        "aws_sdk_efs.types.transition_to_primary_storage_class_rules.TransitionToPrimaryStorageClassRules"
    ]
    """<p>Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.</p>"""
    transition_to_archive: NotRequired[
        "aws_sdk_efs.types.transition_to_archive_rules.TransitionToArchiveRules"
    ]
    """<p>The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicy) -> dict:
    out: dict = {}
    if "transition_to_ia" in value:
        import aws_sdk_efs.types.transition_to_ia_rules

        out["TransitionToIA"] = aws_sdk_efs.types.transition_to_ia_rules.serialize_json(
            value["transition_to_ia"]
        )
    if "transition_to_primary_storage_class" in value:
        import aws_sdk_efs.types.transition_to_primary_storage_class_rules

        out["TransitionToPrimaryStorageClass"] = (
            aws_sdk_efs.types.transition_to_primary_storage_class_rules.serialize_json(
                value["transition_to_primary_storage_class"]
            )
        )
    if "transition_to_archive" in value:
        import aws_sdk_efs.types.transition_to_archive_rules

        out["TransitionToArchive"] = (
            aws_sdk_efs.types.transition_to_archive_rules.serialize_json(
                value["transition_to_archive"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicy:
    out: LifecyclePolicy = {}  # type: ignore[typeddict-item]
    if "TransitionToIA" in data:
        import aws_sdk_efs.types.transition_to_ia_rules

        out["transition_to_ia"] = (
            aws_sdk_efs.types.transition_to_ia_rules.deserialize_json(
                data["TransitionToIA"]
            )
        )
    if "TransitionToPrimaryStorageClass" in data:
        import aws_sdk_efs.types.transition_to_primary_storage_class_rules

        out["transition_to_primary_storage_class"] = (
            aws_sdk_efs.types.transition_to_primary_storage_class_rules.deserialize_json(
                data["TransitionToPrimaryStorageClass"]
            )
        )
    if "TransitionToArchive" in data:
        import aws_sdk_efs.types.transition_to_archive_rules

        out["transition_to_archive"] = (
            aws_sdk_efs.types.transition_to_archive_rules.deserialize_json(
                data["TransitionToArchive"]
            )
        )
    return out
