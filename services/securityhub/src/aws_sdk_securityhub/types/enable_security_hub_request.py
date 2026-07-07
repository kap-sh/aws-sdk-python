"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableSecurityHubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.control_finding_generator
    import aws_sdk_securityhub.types.tag_map


class EnableSecurityHubRequest(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the hub resource when you enable Security Hub CSPM.</p>"""
    enable_default_standards: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to enable the security standards that Security Hub CSPM has designated as automatically enabled. If you don't provide a value for <code>EnableDefaultStandards</code>, it is set to <code>true</code>. To not enable the automatically enabled standards, set <code>EnableDefaultStandards</code> to <code>false</code>.</p>"""
    control_finding_generator: NotRequired[
        "aws_sdk_securityhub.types.control_finding_generator.ControlFindingGenerator"
    ]
    """<p>This field, used when enabling Security Hub CSPM, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is <code>SECURITY_CONTROL</code> if you enabled Security Hub CSPM on or after February 23, 2023.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSecurityHubRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    if "enable_default_standards" in value:
        out["EnableDefaultStandards"] = value["enable_default_standards"]
    if "control_finding_generator" in value:
        import aws_sdk_securityhub.types.control_finding_generator

        out["ControlFindingGenerator"] = (
            aws_sdk_securityhub.types.control_finding_generator.serialize_json(
                value["control_finding_generator"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnableSecurityHubRequest:
    out: EnableSecurityHubRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    if "EnableDefaultStandards" in data:
        out["enable_default_standards"] = data["EnableDefaultStandards"]
    if "ControlFindingGenerator" in data:
        import aws_sdk_securityhub.types.control_finding_generator

        out["control_finding_generator"] = (
            aws_sdk_securityhub.types.control_finding_generator.deserialize_json(
                data["ControlFindingGenerator"]
            )
        )
    return out
