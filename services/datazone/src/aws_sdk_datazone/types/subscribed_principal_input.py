"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipalInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_group_input
    import aws_sdk_datazone.types.subscribed_iam_principal_input
    import aws_sdk_datazone.types.subscribed_project_input
    import aws_sdk_datazone.types.subscribed_user_input


class _SubscribedPrincipalInput_project(TypedDict, closed=True):
    project: "aws_sdk_datazone.types.subscribed_project_input.SubscribedProjectInput"


class _SubscribedPrincipalInput_user(TypedDict, closed=True):
    user: "aws_sdk_datazone.types.subscribed_user_input.SubscribedUserInput"


class _SubscribedPrincipalInput_group(TypedDict, closed=True):
    group: "aws_sdk_datazone.types.subscribed_group_input.SubscribedGroupInput"


class _SubscribedPrincipalInput_iam(TypedDict, closed=True):
    iam: "aws_sdk_datazone.types.subscribed_iam_principal_input.SubscribedIamPrincipalInput"


SubscribedPrincipalInput: TypeAlias = (
    _SubscribedPrincipalInput_project
    | _SubscribedPrincipalInput_user
    | _SubscribedPrincipalInput_group
    | _SubscribedPrincipalInput_iam
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipalInput) -> dict:
    if "project" in value:
        import aws_sdk_datazone.types.subscribed_project_input

        return {
            "project": aws_sdk_datazone.types.subscribed_project_input.serialize_json(
                value["project"]
            )
        }
    elif "user" in value:
        import aws_sdk_datazone.types.subscribed_user_input

        return {
            "user": aws_sdk_datazone.types.subscribed_user_input.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import aws_sdk_datazone.types.subscribed_group_input

        return {
            "group": aws_sdk_datazone.types.subscribed_group_input.serialize_json(
                value["group"]
            )
        }
    elif "iam" in value:
        import aws_sdk_datazone.types.subscribed_iam_principal_input

        return {
            "iam": aws_sdk_datazone.types.subscribed_iam_principal_input.serialize_json(
                value["iam"]
            )
        }
    else:
        raise SerializationError("SubscribedPrincipalInput: no variant present")


def deserialize_json(data: dict) -> SubscribedPrincipalInput:
    if "project" in data:
        import aws_sdk_datazone.types.subscribed_project_input

        return {
            "project": aws_sdk_datazone.types.subscribed_project_input.deserialize_json(
                data["project"]
            )
        }
    elif "user" in data:
        import aws_sdk_datazone.types.subscribed_user_input

        return {
            "user": aws_sdk_datazone.types.subscribed_user_input.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import aws_sdk_datazone.types.subscribed_group_input

        return {
            "group": aws_sdk_datazone.types.subscribed_group_input.deserialize_json(
                data["group"]
            )
        }
    elif "iam" in data:
        import aws_sdk_datazone.types.subscribed_iam_principal_input

        return {
            "iam": aws_sdk_datazone.types.subscribed_iam_principal_input.deserialize_json(
                data["iam"]
            )
        }
    else:
        raise DeserializationError(
            "SubscribedPrincipalInput: no recognized variant key"
        )
