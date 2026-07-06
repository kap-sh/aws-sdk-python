"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cross_region_copy_retain_rule
    import aws_sdk_dlm.types.encryption_configuration
    import aws_sdk_dlm.types.target


class CrossRegionCopyAction(TypedDict, closed=True):
    target: NotRequired["aws_sdk_dlm.types.target.Target"]
    """<p>The target Region.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_dlm.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption settings for the copied snapshot.</p>"""
    retain_rule: NotRequired[
        "aws_sdk_dlm.types.cross_region_copy_retain_rule.CrossRegionCopyRetainRule"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyAction) -> dict:
    out: dict = {}
    if "target" in value:
        out["Target"] = value["target"]
    if "encryption_configuration" in value:
        import aws_sdk_dlm.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_dlm.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "retain_rule" in value:
        import aws_sdk_dlm.types.cross_region_copy_retain_rule

        out["RetainRule"] = (
            aws_sdk_dlm.types.cross_region_copy_retain_rule.serialize_json(
                value["retain_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrossRegionCopyAction:
    out: CrossRegionCopyAction = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        out["target"] = data["Target"]
    if "EncryptionConfiguration" in data:
        import aws_sdk_dlm.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_dlm.types.encryption_configuration.deserialize_json(
                data["EncryptionConfiguration"]
            )
        )
    if "RetainRule" in data:
        import aws_sdk_dlm.types.cross_region_copy_retain_rule

        out["retain_rule"] = (
            aws_sdk_dlm.types.cross_region_copy_retain_rule.deserialize_json(
                data["RetainRule"]
            )
        )
    return out
