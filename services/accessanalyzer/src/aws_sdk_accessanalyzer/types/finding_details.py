"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.external_access_details
    import aws_sdk_accessanalyzer.types.internal_access_details
    import aws_sdk_accessanalyzer.types.unused_iam_role_details
    import aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details
    import aws_sdk_accessanalyzer.types.unused_iam_user_password_details
    import aws_sdk_accessanalyzer.types.unused_permission_details


class _FindingDetails_internalAccessDetails(TypedDict, closed=True):
    internalAccessDetails: (
        "aws_sdk_accessanalyzer.types.internal_access_details.InternalAccessDetails"
    )


class _FindingDetails_externalAccessDetails(TypedDict, closed=True):
    externalAccessDetails: (
        "aws_sdk_accessanalyzer.types.external_access_details.ExternalAccessDetails"
    )


class _FindingDetails_unusedPermissionDetails(TypedDict, closed=True):
    unusedPermissionDetails: (
        "aws_sdk_accessanalyzer.types.unused_permission_details.UnusedPermissionDetails"
    )


class _FindingDetails_unusedIamUserAccessKeyDetails(TypedDict, closed=True):
    unusedIamUserAccessKeyDetails: "aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details.UnusedIamUserAccessKeyDetails"


class _FindingDetails_unusedIamRoleDetails(TypedDict, closed=True):
    unusedIamRoleDetails: (
        "aws_sdk_accessanalyzer.types.unused_iam_role_details.UnusedIamRoleDetails"
    )


class _FindingDetails_unusedIamUserPasswordDetails(TypedDict, closed=True):
    unusedIamUserPasswordDetails: "aws_sdk_accessanalyzer.types.unused_iam_user_password_details.UnusedIamUserPasswordDetails"


FindingDetails: TypeAlias = (
    _FindingDetails_internalAccessDetails
    | _FindingDetails_externalAccessDetails
    | _FindingDetails_unusedPermissionDetails
    | _FindingDetails_unusedIamUserAccessKeyDetails
    | _FindingDetails_unusedIamRoleDetails
    | _FindingDetails_unusedIamUserPasswordDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetails) -> dict:
    if "internalAccessDetails" in value:
        import aws_sdk_accessanalyzer.types.internal_access_details

        return {
            "internalAccessDetails": aws_sdk_accessanalyzer.types.internal_access_details.serialize_json(
                value["internalAccessDetails"]
            )
        }
    elif "externalAccessDetails" in value:
        import aws_sdk_accessanalyzer.types.external_access_details

        return {
            "externalAccessDetails": aws_sdk_accessanalyzer.types.external_access_details.serialize_json(
                value["externalAccessDetails"]
            )
        }
    elif "unusedPermissionDetails" in value:
        import aws_sdk_accessanalyzer.types.unused_permission_details

        return {
            "unusedPermissionDetails": aws_sdk_accessanalyzer.types.unused_permission_details.serialize_json(
                value["unusedPermissionDetails"]
            )
        }
    elif "unusedIamUserAccessKeyDetails" in value:
        import aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details

        return {
            "unusedIamUserAccessKeyDetails": aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details.serialize_json(
                value["unusedIamUserAccessKeyDetails"]
            )
        }
    elif "unusedIamRoleDetails" in value:
        import aws_sdk_accessanalyzer.types.unused_iam_role_details

        return {
            "unusedIamRoleDetails": aws_sdk_accessanalyzer.types.unused_iam_role_details.serialize_json(
                value["unusedIamRoleDetails"]
            )
        }
    elif "unusedIamUserPasswordDetails" in value:
        import aws_sdk_accessanalyzer.types.unused_iam_user_password_details

        return {
            "unusedIamUserPasswordDetails": aws_sdk_accessanalyzer.types.unused_iam_user_password_details.serialize_json(
                value["unusedIamUserPasswordDetails"]
            )
        }
    else:
        raise SerializationError("FindingDetails: no variant present")


def deserialize_json(data: dict) -> FindingDetails:
    if "internalAccessDetails" in data:
        import aws_sdk_accessanalyzer.types.internal_access_details

        return {
            "internalAccessDetails": aws_sdk_accessanalyzer.types.internal_access_details.deserialize_json(
                data["internalAccessDetails"]
            )
        }
    elif "externalAccessDetails" in data:
        import aws_sdk_accessanalyzer.types.external_access_details

        return {
            "externalAccessDetails": aws_sdk_accessanalyzer.types.external_access_details.deserialize_json(
                data["externalAccessDetails"]
            )
        }
    elif "unusedPermissionDetails" in data:
        import aws_sdk_accessanalyzer.types.unused_permission_details

        return {
            "unusedPermissionDetails": aws_sdk_accessanalyzer.types.unused_permission_details.deserialize_json(
                data["unusedPermissionDetails"]
            )
        }
    elif "unusedIamUserAccessKeyDetails" in data:
        import aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details

        return {
            "unusedIamUserAccessKeyDetails": aws_sdk_accessanalyzer.types.unused_iam_user_access_key_details.deserialize_json(
                data["unusedIamUserAccessKeyDetails"]
            )
        }
    elif "unusedIamRoleDetails" in data:
        import aws_sdk_accessanalyzer.types.unused_iam_role_details

        return {
            "unusedIamRoleDetails": aws_sdk_accessanalyzer.types.unused_iam_role_details.deserialize_json(
                data["unusedIamRoleDetails"]
            )
        }
    elif "unusedIamUserPasswordDetails" in data:
        import aws_sdk_accessanalyzer.types.unused_iam_user_password_details

        return {
            "unusedIamUserPasswordDetails": aws_sdk_accessanalyzer.types.unused_iam_user_password_details.deserialize_json(
                data["unusedIamUserPasswordDetails"]
            )
        }
    else:
        raise DeserializationError("FindingDetails: no recognized variant key")
