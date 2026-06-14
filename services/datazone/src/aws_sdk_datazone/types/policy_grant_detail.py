"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantDetail``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail
    import aws_sdk_datazone.types.create_asset_type_policy_grant_detail
    import aws_sdk_datazone.types.create_domain_unit_policy_grant_detail
    import aws_sdk_datazone.types.create_environment_profile_policy_grant_detail
    import aws_sdk_datazone.types.create_form_type_policy_grant_detail
    import aws_sdk_datazone.types.create_glossary_policy_grant_detail
    import aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail
    import aws_sdk_datazone.types.create_project_policy_grant_detail
    import aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail
    import aws_sdk_datazone.types.override_project_owners_policy_grant_detail
    import aws_sdk_datazone.types.unit
    import aws_sdk_datazone.types.use_asset_type_policy_grant_detail


class _PolicyGrantDetail_createDomainUnit(TypedDict):
    createDomainUnit: "aws_sdk_datazone.types.create_domain_unit_policy_grant_detail.CreateDomainUnitPolicyGrantDetail"


class _PolicyGrantDetail_overrideDomainUnitOwners(TypedDict):
    overrideDomainUnitOwners: "aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail.OverrideDomainUnitOwnersPolicyGrantDetail"


class _PolicyGrantDetail_addToProjectMemberPool(TypedDict):
    addToProjectMemberPool: "aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail.AddToProjectMemberPoolPolicyGrantDetail"


class _PolicyGrantDetail_overrideProjectOwners(TypedDict):
    overrideProjectOwners: "aws_sdk_datazone.types.override_project_owners_policy_grant_detail.OverrideProjectOwnersPolicyGrantDetail"


class _PolicyGrantDetail_createGlossary(TypedDict):
    createGlossary: "aws_sdk_datazone.types.create_glossary_policy_grant_detail.CreateGlossaryPolicyGrantDetail"


class _PolicyGrantDetail_createFormType(TypedDict):
    createFormType: "aws_sdk_datazone.types.create_form_type_policy_grant_detail.CreateFormTypePolicyGrantDetail"


class _PolicyGrantDetail_createAssetType(TypedDict):
    createAssetType: "aws_sdk_datazone.types.create_asset_type_policy_grant_detail.CreateAssetTypePolicyGrantDetail"


class _PolicyGrantDetail_createProject(TypedDict):
    createProject: "aws_sdk_datazone.types.create_project_policy_grant_detail.CreateProjectPolicyGrantDetail"


class _PolicyGrantDetail_createEnvironmentProfile(TypedDict):
    createEnvironmentProfile: "aws_sdk_datazone.types.create_environment_profile_policy_grant_detail.CreateEnvironmentProfilePolicyGrantDetail"


class _PolicyGrantDetail_delegateCreateEnvironmentProfile(TypedDict):
    delegateCreateEnvironmentProfile: "aws_sdk_datazone.types.unit.Unit"


class _PolicyGrantDetail_createEnvironment(TypedDict):
    createEnvironment: "aws_sdk_datazone.types.unit.Unit"


class _PolicyGrantDetail_createEnvironmentFromBlueprint(TypedDict):
    createEnvironmentFromBlueprint: "aws_sdk_datazone.types.unit.Unit"


class _PolicyGrantDetail_createProjectFromProjectProfile(TypedDict):
    createProjectFromProjectProfile: "aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail.CreateProjectFromProjectProfilePolicyGrantDetail"


class _PolicyGrantDetail_useAssetType(TypedDict):
    useAssetType: "aws_sdk_datazone.types.use_asset_type_policy_grant_detail.UseAssetTypePolicyGrantDetail"


PolicyGrantDetail: TypeAlias = (
    _PolicyGrantDetail_createDomainUnit
    | _PolicyGrantDetail_overrideDomainUnitOwners
    | _PolicyGrantDetail_addToProjectMemberPool
    | _PolicyGrantDetail_overrideProjectOwners
    | _PolicyGrantDetail_createGlossary
    | _PolicyGrantDetail_createFormType
    | _PolicyGrantDetail_createAssetType
    | _PolicyGrantDetail_createProject
    | _PolicyGrantDetail_createEnvironmentProfile
    | _PolicyGrantDetail_delegateCreateEnvironmentProfile
    | _PolicyGrantDetail_createEnvironment
    | _PolicyGrantDetail_createEnvironmentFromBlueprint
    | _PolicyGrantDetail_createProjectFromProjectProfile
    | _PolicyGrantDetail_useAssetType
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantDetail) -> dict:
    if "createDomainUnit" in value:
        import aws_sdk_datazone.types.create_domain_unit_policy_grant_detail

        return {
            "createDomainUnit": aws_sdk_datazone.types.create_domain_unit_policy_grant_detail.serialize_json(
                value["createDomainUnit"]
            )
        }
    elif "overrideDomainUnitOwners" in value:
        import aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail

        return {
            "overrideDomainUnitOwners": aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail.serialize_json(
                value["overrideDomainUnitOwners"]
            )
        }
    elif "addToProjectMemberPool" in value:
        import aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail

        return {
            "addToProjectMemberPool": aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail.serialize_json(
                value["addToProjectMemberPool"]
            )
        }
    elif "overrideProjectOwners" in value:
        import aws_sdk_datazone.types.override_project_owners_policy_grant_detail

        return {
            "overrideProjectOwners": aws_sdk_datazone.types.override_project_owners_policy_grant_detail.serialize_json(
                value["overrideProjectOwners"]
            )
        }
    elif "createGlossary" in value:
        import aws_sdk_datazone.types.create_glossary_policy_grant_detail

        return {
            "createGlossary": aws_sdk_datazone.types.create_glossary_policy_grant_detail.serialize_json(
                value["createGlossary"]
            )
        }
    elif "createFormType" in value:
        import aws_sdk_datazone.types.create_form_type_policy_grant_detail

        return {
            "createFormType": aws_sdk_datazone.types.create_form_type_policy_grant_detail.serialize_json(
                value["createFormType"]
            )
        }
    elif "createAssetType" in value:
        import aws_sdk_datazone.types.create_asset_type_policy_grant_detail

        return {
            "createAssetType": aws_sdk_datazone.types.create_asset_type_policy_grant_detail.serialize_json(
                value["createAssetType"]
            )
        }
    elif "createProject" in value:
        import aws_sdk_datazone.types.create_project_policy_grant_detail

        return {
            "createProject": aws_sdk_datazone.types.create_project_policy_grant_detail.serialize_json(
                value["createProject"]
            )
        }
    elif "createEnvironmentProfile" in value:
        import aws_sdk_datazone.types.create_environment_profile_policy_grant_detail

        return {
            "createEnvironmentProfile": aws_sdk_datazone.types.create_environment_profile_policy_grant_detail.serialize_json(
                value["createEnvironmentProfile"]
            )
        }
    elif "delegateCreateEnvironmentProfile" in value:
        import aws_sdk_datazone.types.unit

        return {
            "delegateCreateEnvironmentProfile": aws_sdk_datazone.types.unit.serialize_json(
                value["delegateCreateEnvironmentProfile"]
            )
        }
    elif "createEnvironment" in value:
        import aws_sdk_datazone.types.unit

        return {
            "createEnvironment": aws_sdk_datazone.types.unit.serialize_json(
                value["createEnvironment"]
            )
        }
    elif "createEnvironmentFromBlueprint" in value:
        import aws_sdk_datazone.types.unit

        return {
            "createEnvironmentFromBlueprint": aws_sdk_datazone.types.unit.serialize_json(
                value["createEnvironmentFromBlueprint"]
            )
        }
    elif "createProjectFromProjectProfile" in value:
        import aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail

        return {
            "createProjectFromProjectProfile": aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail.serialize_json(
                value["createProjectFromProjectProfile"]
            )
        }
    elif "useAssetType" in value:
        import aws_sdk_datazone.types.use_asset_type_policy_grant_detail

        return {
            "useAssetType": aws_sdk_datazone.types.use_asset_type_policy_grant_detail.serialize_json(
                value["useAssetType"]
            )
        }
    else:
        raise SerializationError("PolicyGrantDetail: no variant present")


def deserialize_json(data: dict) -> PolicyGrantDetail:
    if "createDomainUnit" in data:
        import aws_sdk_datazone.types.create_domain_unit_policy_grant_detail

        return {
            "createDomainUnit": aws_sdk_datazone.types.create_domain_unit_policy_grant_detail.deserialize_json(
                data["createDomainUnit"]
            )
        }
    elif "overrideDomainUnitOwners" in data:
        import aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail

        return {
            "overrideDomainUnitOwners": aws_sdk_datazone.types.override_domain_unit_owners_policy_grant_detail.deserialize_json(
                data["overrideDomainUnitOwners"]
            )
        }
    elif "addToProjectMemberPool" in data:
        import aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail

        return {
            "addToProjectMemberPool": aws_sdk_datazone.types.add_to_project_member_pool_policy_grant_detail.deserialize_json(
                data["addToProjectMemberPool"]
            )
        }
    elif "overrideProjectOwners" in data:
        import aws_sdk_datazone.types.override_project_owners_policy_grant_detail

        return {
            "overrideProjectOwners": aws_sdk_datazone.types.override_project_owners_policy_grant_detail.deserialize_json(
                data["overrideProjectOwners"]
            )
        }
    elif "createGlossary" in data:
        import aws_sdk_datazone.types.create_glossary_policy_grant_detail

        return {
            "createGlossary": aws_sdk_datazone.types.create_glossary_policy_grant_detail.deserialize_json(
                data["createGlossary"]
            )
        }
    elif "createFormType" in data:
        import aws_sdk_datazone.types.create_form_type_policy_grant_detail

        return {
            "createFormType": aws_sdk_datazone.types.create_form_type_policy_grant_detail.deserialize_json(
                data["createFormType"]
            )
        }
    elif "createAssetType" in data:
        import aws_sdk_datazone.types.create_asset_type_policy_grant_detail

        return {
            "createAssetType": aws_sdk_datazone.types.create_asset_type_policy_grant_detail.deserialize_json(
                data["createAssetType"]
            )
        }
    elif "createProject" in data:
        import aws_sdk_datazone.types.create_project_policy_grant_detail

        return {
            "createProject": aws_sdk_datazone.types.create_project_policy_grant_detail.deserialize_json(
                data["createProject"]
            )
        }
    elif "createEnvironmentProfile" in data:
        import aws_sdk_datazone.types.create_environment_profile_policy_grant_detail

        return {
            "createEnvironmentProfile": aws_sdk_datazone.types.create_environment_profile_policy_grant_detail.deserialize_json(
                data["createEnvironmentProfile"]
            )
        }
    elif "delegateCreateEnvironmentProfile" in data:
        import aws_sdk_datazone.types.unit

        return {
            "delegateCreateEnvironmentProfile": aws_sdk_datazone.types.unit.deserialize_json(
                data["delegateCreateEnvironmentProfile"]
            )
        }
    elif "createEnvironment" in data:
        import aws_sdk_datazone.types.unit

        return {
            "createEnvironment": aws_sdk_datazone.types.unit.deserialize_json(
                data["createEnvironment"]
            )
        }
    elif "createEnvironmentFromBlueprint" in data:
        import aws_sdk_datazone.types.unit

        return {
            "createEnvironmentFromBlueprint": aws_sdk_datazone.types.unit.deserialize_json(
                data["createEnvironmentFromBlueprint"]
            )
        }
    elif "createProjectFromProjectProfile" in data:
        import aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail

        return {
            "createProjectFromProjectProfile": aws_sdk_datazone.types.create_project_from_project_profile_policy_grant_detail.deserialize_json(
                data["createProjectFromProjectProfile"]
            )
        }
    elif "useAssetType" in data:
        import aws_sdk_datazone.types.use_asset_type_policy_grant_detail

        return {
            "useAssetType": aws_sdk_datazone.types.use_asset_type_policy_grant_detail.deserialize_json(
                data["useAssetType"]
            )
        }
    else:
        raise DeserializationError("PolicyGrantDetail: no recognized variant key")
