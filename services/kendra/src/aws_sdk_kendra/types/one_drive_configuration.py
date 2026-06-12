"""Generated from Smithy shape ``com.amazonaws.kendra#OneDriveConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list
    import aws_sdk_kendra.types.one_drive_users
    import aws_sdk_kendra.types.secret_arn
    import aws_sdk_kendra.types.tenant_domain


class OneDriveConfiguration(TypedDict):
    tenant_domain: "aws_sdk_kendra.types.tenant_domain.TenantDomain"
    """<p>The Azure Active Directory domain of the organization. </p>"""
    secret_arn: "aws_sdk_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the user name and password to connect to OneDrive. The user name should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.</p>"""
    one_drive_users: "aws_sdk_kendra.types.one_drive_users.OneDriveUsers"
    """<p>A list of user accounts whose documents should be indexed.</p>"""
    inclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain documents in your OneDrive. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the file name.</p>"""
    exclusion_patterns: NotRequired[
        "aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain documents in your OneDrive. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.</p> <p>The pattern is applied to the file name.</p>"""
    field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map OneDrive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to OneDrive fields. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html\">Mapping data source fields</a>. The OneDrive data source field names must exist in your OneDrive custom metadata.</p>"""
    disable_local_groups: "aws_sdk_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to disable local groups information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OneDriveConfiguration) -> dict:
    out: dict = {}
    out["TenantDomain"] = value["tenant_domain"]
    out["SecretArn"] = value["secret_arn"]
    import aws_sdk_kendra.types.one_drive_users

    out["OneDriveUsers"] = aws_sdk_kendra.types.one_drive_users.serialize_aws_json_1_1(
        value["one_drive_users"]
    )
    if "inclusion_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["InclusionPatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["inclusion_patterns"]
            )
        )
    if "exclusion_patterns" in value:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["ExclusionPatterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclusion_patterns"]
            )
        )
    if "field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    out["DisableLocalGroups"] = value.get("disable_local_groups", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> OneDriveConfiguration:
    out: OneDriveConfiguration = {}  # type: ignore[typeddict-item]
    if "TenantDomain" in data:
        out["tenant_domain"] = data["TenantDomain"]
    else:
        raise DeserializationError("OneDriveConfiguration.tenant_domain required")
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("OneDriveConfiguration.secret_arn required")
    if "OneDriveUsers" in data:
        import aws_sdk_kendra.types.one_drive_users

        out["one_drive_users"] = (
            aws_sdk_kendra.types.one_drive_users.deserialize_aws_json_1_1(
                data["OneDriveUsers"]
            )
        )
    else:
        raise DeserializationError("OneDriveConfiguration.one_drive_users required")
    if "InclusionPatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["inclusion_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["InclusionPatterns"]
            )
        )
    if "ExclusionPatterns" in data:
        import aws_sdk_kendra.types.data_source_inclusions_exclusions_strings

        out["exclusion_patterns"] = (
            aws_sdk_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExclusionPatterns"]
            )
        )
    if "FieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if "DisableLocalGroups" in data:
        out["disable_local_groups"] = data["DisableLocalGroups"]
    else:
        out["disable_local_groups"] = False
    return out
