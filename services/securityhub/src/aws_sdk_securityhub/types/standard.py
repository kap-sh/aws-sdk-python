"""Generated from Smithy shape ``com.amazonaws.securityhub#Standard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.standards_managed_by


class Standard(TypedDict, closed=True):
    standards_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the standard.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the standard.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the standard.</p>"""
    enabled_by_default: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the standard is enabled by default. When Security Hub CSPM is enabled from the console, if a standard is enabled by default, the check box for that standard is selected by default.</p> <p>When Security Hub CSPM is enabled using the <code>EnableSecurityHub</code> API operation, the standard is enabled by default unless <code>EnableDefaultStandards</code> is set to <code>false</code>.</p>"""
    standards_managed_by: NotRequired[
        "aws_sdk_securityhub.types.standards_managed_by.StandardsManagedBy"
    ]
    """<p>Provides details about the management of a standard. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Standard) -> dict:
    out: dict = {}
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "enabled_by_default" in value:
        out["EnabledByDefault"] = value["enabled_by_default"]
    if "standards_managed_by" in value:
        import aws_sdk_securityhub.types.standards_managed_by

        out["StandardsManagedBy"] = (
            aws_sdk_securityhub.types.standards_managed_by.serialize_json(
                value["standards_managed_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> Standard:
    out: Standard = {}  # type: ignore[typeddict-item]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EnabledByDefault" in data:
        out["enabled_by_default"] = data["EnabledByDefault"]
    if "StandardsManagedBy" in data:
        import aws_sdk_securityhub.types.standards_managed_by

        out["standards_managed_by"] = (
            aws_sdk_securityhub.types.standards_managed_by.deserialize_json(
                data["StandardsManagedBy"]
            )
        )
    return out
