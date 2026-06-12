"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RoleMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.ambiguous_role_resolution_type
    import aws_sdk_cognito_identity.types.role_mapping_type
    import aws_sdk_cognito_identity.types.rules_configuration_type


class RoleMapping(TypedDict):
    type: "aws_sdk_cognito_identity.types.role_mapping_type.RoleMappingType"
    """<p>The role mapping type. Token will use <code>cognito:roles</code> and <code>cognito:preferred_role</code> claims from the Cognito identity provider token to map groups to roles. Rules will attempt to match claims from the token to map to a role.</p>"""
    ambiguous_role_resolution: NotRequired[
        "aws_sdk_cognito_identity.types.ambiguous_role_resolution_type.AmbiguousRoleResolutionType"
    ]
    """<p>If you specify Token or Rules as the <code>Type</code>, <code>AmbiguousRoleResolution</code> is required.</p> <p>Specifies the action to be taken if either no rules match the claim value for the <code>Rules</code> type, or there is no <code>cognito:preferred_role</code> claim and there are multiple <code>cognito:roles</code> matches for the <code>Token</code> type.</p>"""
    rules_configuration: NotRequired[
        "aws_sdk_cognito_identity.types.rules_configuration_type.RulesConfigurationType"
    ]
    """<p>The rules to be used for mapping users to roles.</p> <p>If you specify Rules as the role mapping type, <code>RulesConfiguration</code> is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoleMapping) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity.types.role_mapping_type

    out["Type"] = (
        aws_sdk_cognito_identity.types.role_mapping_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "ambiguous_role_resolution" in value:
        import aws_sdk_cognito_identity.types.ambiguous_role_resolution_type

        out["AmbiguousRoleResolution"] = (
            aws_sdk_cognito_identity.types.ambiguous_role_resolution_type.serialize_aws_json_1_1(
                value["ambiguous_role_resolution"]
            )
        )
    if "rules_configuration" in value:
        import aws_sdk_cognito_identity.types.rules_configuration_type

        out["RulesConfiguration"] = (
            aws_sdk_cognito_identity.types.rules_configuration_type.serialize_aws_json_1_1(
                value["rules_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoleMapping:
    out: RoleMapping = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_cognito_identity.types.role_mapping_type

        out["type"] = (
            aws_sdk_cognito_identity.types.role_mapping_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RoleMapping.type required")
    if "AmbiguousRoleResolution" in data:
        import aws_sdk_cognito_identity.types.ambiguous_role_resolution_type

        out["ambiguous_role_resolution"] = (
            aws_sdk_cognito_identity.types.ambiguous_role_resolution_type.deserialize_aws_json_1_1(
                data["AmbiguousRoleResolution"]
            )
        )
    if "RulesConfiguration" in data:
        import aws_sdk_cognito_identity.types.rules_configuration_type

        out["rules_configuration"] = (
            aws_sdk_cognito_identity.types.rules_configuration_type.deserialize_aws_json_1_1(
                data["RulesConfiguration"]
            )
        )
    return out
