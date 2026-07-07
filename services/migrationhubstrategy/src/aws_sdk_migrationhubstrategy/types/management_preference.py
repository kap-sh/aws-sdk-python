"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ManagementPreference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.aws_managed_resources
    import aws_sdk_migrationhubstrategy.types.no_management_preference
    import aws_sdk_migrationhubstrategy.types.self_manage_resources


class _ManagementPreference_awsManagedResources(TypedDict, closed=True):
    awsManagedResources: (
        "aws_sdk_migrationhubstrategy.types.aws_managed_resources.AwsManagedResources"
    )


class _ManagementPreference_selfManageResources(TypedDict, closed=True):
    selfManageResources: (
        "aws_sdk_migrationhubstrategy.types.self_manage_resources.SelfManageResources"
    )


class _ManagementPreference_noPreference(TypedDict, closed=True):
    noPreference: "aws_sdk_migrationhubstrategy.types.no_management_preference.NoManagementPreference"


ManagementPreference: TypeAlias = (
    _ManagementPreference_awsManagedResources
    | _ManagementPreference_selfManageResources
    | _ManagementPreference_noPreference
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagementPreference) -> dict:
    if "awsManagedResources" in value:
        import aws_sdk_migrationhubstrategy.types.aws_managed_resources

        return {
            "awsManagedResources": aws_sdk_migrationhubstrategy.types.aws_managed_resources.serialize_json(
                value["awsManagedResources"]
            )
        }
    elif "selfManageResources" in value:
        import aws_sdk_migrationhubstrategy.types.self_manage_resources

        return {
            "selfManageResources": aws_sdk_migrationhubstrategy.types.self_manage_resources.serialize_json(
                value["selfManageResources"]
            )
        }
    elif "noPreference" in value:
        import aws_sdk_migrationhubstrategy.types.no_management_preference

        return {
            "noPreference": aws_sdk_migrationhubstrategy.types.no_management_preference.serialize_json(
                value["noPreference"]
            )
        }
    else:
        raise SerializationError("ManagementPreference: no variant present")


def deserialize_json(data: dict) -> ManagementPreference:
    if "awsManagedResources" in data:
        import aws_sdk_migrationhubstrategy.types.aws_managed_resources

        return {
            "awsManagedResources": aws_sdk_migrationhubstrategy.types.aws_managed_resources.deserialize_json(
                data["awsManagedResources"]
            )
        }
    elif "selfManageResources" in data:
        import aws_sdk_migrationhubstrategy.types.self_manage_resources

        return {
            "selfManageResources": aws_sdk_migrationhubstrategy.types.self_manage_resources.deserialize_json(
                data["selfManageResources"]
            )
        }
    elif "noPreference" in data:
        import aws_sdk_migrationhubstrategy.types.no_management_preference

        return {
            "noPreference": aws_sdk_migrationhubstrategy.types.no_management_preference.deserialize_json(
                data["noPreference"]
            )
        }
    else:
        raise DeserializationError("ManagementPreference: no recognized variant key")
