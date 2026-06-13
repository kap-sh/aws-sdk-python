"""Generated from Smithy shape ``com.amazonaws.backup#ResourceSelection``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.resource_arns
    import aws_sdk_backup.types.resource_type
    import aws_sdk_backup.types.tiering_down_settings_in_days


class ResourceSelection(TypedDict):
    resources: "aws_sdk_backup.types.resource_arns.ResourceArns"
    """<p>An array of strings that either contains ARNs of the associated resources or contains a wildcard <code>*</code> to specify all resources. You can specify up to 100 specific resources per tiering configuration.</p>"""
    tiering_down_settings_in_days: (
        "aws_sdk_backup.types.tiering_down_settings_in_days.TieringDownSettingsInDays"
    )
    """<p>The number of days after creation within a backup vault that an object can transition to the low cost warm storage tier. Must be a positive integer between 60 and 36500 days.</p>"""
    resource_type: "aws_sdk_backup.types.resource_type.ResourceType"
    """<p>The type of Amazon Web Services resource; for example, <code>S3</code> for Amazon S3. For tiering configurations, this is currently limited to <code>S3</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSelection) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.resource_arns

    out["Resources"] = aws_sdk_backup.types.resource_arns.serialize_json(
        value["resources"]
    )
    out["TieringDownSettingsInDays"] = value["tiering_down_settings_in_days"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceSelection:
    out: ResourceSelection = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_backup.types.resource_arns

        out["resources"] = aws_sdk_backup.types.resource_arns.deserialize_json(
            data["Resources"]
        )
    else:
        raise DeserializationError("ResourceSelection.resources required")
    if "TieringDownSettingsInDays" in data:
        out["tiering_down_settings_in_days"] = data["TieringDownSettingsInDays"]
    else:
        raise DeserializationError(
            "ResourceSelection.tiering_down_settings_in_days required"
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceSelection.resource_type required")
    return out
