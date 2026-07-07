"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_unit_policy_grant_principal
    import aws_sdk_datazone.types.group_policy_grant_principal
    import aws_sdk_datazone.types.project_policy_grant_principal
    import aws_sdk_datazone.types.user_policy_grant_principal


class _PolicyGrantPrincipal_user(TypedDict, closed=True):
    user: "aws_sdk_datazone.types.user_policy_grant_principal.UserPolicyGrantPrincipal"


class _PolicyGrantPrincipal_group(TypedDict, closed=True):
    group: (
        "aws_sdk_datazone.types.group_policy_grant_principal.GroupPolicyGrantPrincipal"
    )


class _PolicyGrantPrincipal_project(TypedDict, closed=True):
    project: "aws_sdk_datazone.types.project_policy_grant_principal.ProjectPolicyGrantPrincipal"


class _PolicyGrantPrincipal_domainUnit(TypedDict, closed=True):
    domainUnit: "aws_sdk_datazone.types.domain_unit_policy_grant_principal.DomainUnitPolicyGrantPrincipal"


PolicyGrantPrincipal: TypeAlias = (
    _PolicyGrantPrincipal_user
    | _PolicyGrantPrincipal_group
    | _PolicyGrantPrincipal_project
    | _PolicyGrantPrincipal_domainUnit
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantPrincipal) -> dict:
    if "user" in value:
        import aws_sdk_datazone.types.user_policy_grant_principal

        return {
            "user": aws_sdk_datazone.types.user_policy_grant_principal.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import aws_sdk_datazone.types.group_policy_grant_principal

        return {
            "group": aws_sdk_datazone.types.group_policy_grant_principal.serialize_json(
                value["group"]
            )
        }
    elif "project" in value:
        import aws_sdk_datazone.types.project_policy_grant_principal

        return {
            "project": aws_sdk_datazone.types.project_policy_grant_principal.serialize_json(
                value["project"]
            )
        }
    elif "domainUnit" in value:
        import aws_sdk_datazone.types.domain_unit_policy_grant_principal

        return {
            "domainUnit": aws_sdk_datazone.types.domain_unit_policy_grant_principal.serialize_json(
                value["domainUnit"]
            )
        }
    else:
        raise SerializationError("PolicyGrantPrincipal: no variant present")


def deserialize_json(data: dict) -> PolicyGrantPrincipal:
    if "user" in data:
        import aws_sdk_datazone.types.user_policy_grant_principal

        return {
            "user": aws_sdk_datazone.types.user_policy_grant_principal.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import aws_sdk_datazone.types.group_policy_grant_principal

        return {
            "group": aws_sdk_datazone.types.group_policy_grant_principal.deserialize_json(
                data["group"]
            )
        }
    elif "project" in data:
        import aws_sdk_datazone.types.project_policy_grant_principal

        return {
            "project": aws_sdk_datazone.types.project_policy_grant_principal.deserialize_json(
                data["project"]
            )
        }
    elif "domainUnit" in data:
        import aws_sdk_datazone.types.domain_unit_policy_grant_principal

        return {
            "domainUnit": aws_sdk_datazone.types.domain_unit_policy_grant_principal.deserialize_json(
                data["domainUnit"]
            )
        }
    else:
        raise DeserializationError("PolicyGrantPrincipal: no recognized variant key")
