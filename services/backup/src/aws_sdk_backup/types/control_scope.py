"""Generated from Smithy shape ``com.amazonaws.backup#ControlScope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.compliance_resource_id_list
    import aws_sdk_backup.types.resource_type_list
    import aws_sdk_backup.types.string_map


class ControlScope(TypedDict):
    compliance_resource_ids: NotRequired[
        "aws_sdk_backup.types.compliance_resource_id_list.ComplianceResourceIdList"
    ]
    """<p>The ID of the only Amazon Web Services resource that you want your control scope to contain.</p>"""
    compliance_resource_types: NotRequired[
        "aws_sdk_backup.types.resource_type_list.ResourceTypeList"
    ]
    """<p>Describes whether the control scope includes one or more types of resources, such as <code>EFS</code> or <code>RDS</code>.</p>"""
    tags: NotRequired["aws_sdk_backup.types.string_map.stringMap"]
    """<p>The tag key-value pair applied to those Amazon Web Services resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).</p> <p>The structure to assign a tag is: <code>[{\"Key\":\"string\",\"Value\":\"string\"}]</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlScope) -> dict:
    out: dict = {}
    if "compliance_resource_ids" in value:
        import aws_sdk_backup.types.compliance_resource_id_list

        out["ComplianceResourceIds"] = (
            aws_sdk_backup.types.compliance_resource_id_list.serialize_json(
                value["compliance_resource_ids"]
            )
        )
    if "compliance_resource_types" in value:
        import aws_sdk_backup.types.resource_type_list

        out["ComplianceResourceTypes"] = (
            aws_sdk_backup.types.resource_type_list.serialize_json(
                value["compliance_resource_types"]
            )
        )
    if "tags" in value:
        import aws_sdk_backup.types.string_map

        out["Tags"] = aws_sdk_backup.types.string_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ControlScope:
    out: ControlScope = {}  # type: ignore[typeddict-item]
    if "ComplianceResourceIds" in data:
        import aws_sdk_backup.types.compliance_resource_id_list

        out["compliance_resource_ids"] = (
            aws_sdk_backup.types.compliance_resource_id_list.deserialize_json(
                data["ComplianceResourceIds"]
            )
        )
    if "ComplianceResourceTypes" in data:
        import aws_sdk_backup.types.resource_type_list

        out["compliance_resource_types"] = (
            aws_sdk_backup.types.resource_type_list.deserialize_json(
                data["ComplianceResourceTypes"]
            )
        )
    if "Tags" in data:
        import aws_sdk_backup.types.string_map

        out["tags"] = aws_sdk_backup.types.string_map.deserialize_json(data["Tags"])
    return out
