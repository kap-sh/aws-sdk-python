"""Generated from Smithy shape ``com.amazonaws.opensearch#IdentityCenterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.identity_center_application_arn
    import aws_sdk_opensearch.types.identity_center_instance_arn
    import aws_sdk_opensearch.types.identity_store_id
    import aws_sdk_opensearch.types.region
    import aws_sdk_opensearch.types.roles_key_id_c_option
    import aws_sdk_opensearch.types.subject_key_id_c_option


class IdentityCenterOptions(TypedDict, closed=True):
    enabled_api_access: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether IAM Identity Center is enabled for the application.</p>"""
    identity_center_instance_arn: NotRequired[
        "aws_sdk_opensearch.types.identity_center_instance_arn.IdentityCenterInstanceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance.</p>"""
    identity_center_instance_region: NotRequired[
        "aws_sdk_opensearch.types.region.Region"
    ]
    """<p>The Region of the IAM Identity Center instance.</p>"""
    subject_key: NotRequired[
        "aws_sdk_opensearch.types.subject_key_id_c_option.SubjectKeyIdCOption"
    ]
    """<p>Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.</p>"""
    roles_key: NotRequired[
        "aws_sdk_opensearch.types.roles_key_id_c_option.RolesKeyIdCOption"
    ]
    """<p>Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.</p>"""
    identity_center_application_arn: NotRequired[
        "aws_sdk_opensearch.types.identity_center_application_arn.IdentityCenterApplicationARN"
    ]
    """<p>The ARN of the IAM Identity Center application that integrates with Amazon OpenSearch Service.</p>"""
    identity_store_id: NotRequired[
        "aws_sdk_opensearch.types.identity_store_id.IdentityStoreId"
    ]
    """<p>The identifier of the IAM Identity Store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterOptions) -> dict:
    out: dict = {}
    if "enabled_api_access" in value:
        out["EnabledAPIAccess"] = value["enabled_api_access"]
    if "identity_center_instance_arn" in value:
        out["IdentityCenterInstanceARN"] = value["identity_center_instance_arn"]
    if "identity_center_instance_region" in value:
        out["IdentityCenterInstanceRegion"] = value["identity_center_instance_region"]
    if "subject_key" in value:
        import aws_sdk_opensearch.types.subject_key_id_c_option

        out["SubjectKey"] = (
            aws_sdk_opensearch.types.subject_key_id_c_option.serialize_json(
                value["subject_key"]
            )
        )
    if "roles_key" in value:
        import aws_sdk_opensearch.types.roles_key_id_c_option

        out["RolesKey"] = aws_sdk_opensearch.types.roles_key_id_c_option.serialize_json(
            value["roles_key"]
        )
    if "identity_center_application_arn" in value:
        out["IdentityCenterApplicationARN"] = value["identity_center_application_arn"]
    if "identity_store_id" in value:
        out["IdentityStoreId"] = value["identity_store_id"]
    return out


def deserialize_json(data: dict) -> IdentityCenterOptions:
    out: IdentityCenterOptions = {}  # type: ignore[typeddict-item]
    if "EnabledAPIAccess" in data:
        out["enabled_api_access"] = data["EnabledAPIAccess"]
    if "IdentityCenterInstanceARN" in data:
        out["identity_center_instance_arn"] = data["IdentityCenterInstanceARN"]
    if "IdentityCenterInstanceRegion" in data:
        out["identity_center_instance_region"] = data["IdentityCenterInstanceRegion"]
    if "SubjectKey" in data:
        import aws_sdk_opensearch.types.subject_key_id_c_option

        out["subject_key"] = (
            aws_sdk_opensearch.types.subject_key_id_c_option.deserialize_json(
                data["SubjectKey"]
            )
        )
    if "RolesKey" in data:
        import aws_sdk_opensearch.types.roles_key_id_c_option

        out["roles_key"] = (
            aws_sdk_opensearch.types.roles_key_id_c_option.deserialize_json(
                data["RolesKey"]
            )
        )
    if "IdentityCenterApplicationARN" in data:
        out["identity_center_application_arn"] = data["IdentityCenterApplicationARN"]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    return out
