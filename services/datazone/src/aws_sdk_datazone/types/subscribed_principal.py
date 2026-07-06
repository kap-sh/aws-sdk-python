"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscribed_group
    import aws_sdk_datazone.types.subscribed_iam_principal
    import aws_sdk_datazone.types.subscribed_project
    import aws_sdk_datazone.types.subscribed_user


class _SubscribedPrincipal_project(TypedDict, closed=True):
    project: "aws_sdk_datazone.types.subscribed_project.SubscribedProject"


class _SubscribedPrincipal_user(TypedDict, closed=True):
    user: "aws_sdk_datazone.types.subscribed_user.SubscribedUser"


class _SubscribedPrincipal_group(TypedDict, closed=True):
    group: "aws_sdk_datazone.types.subscribed_group.SubscribedGroup"


class _SubscribedPrincipal_iam(TypedDict, closed=True):
    iam: "aws_sdk_datazone.types.subscribed_iam_principal.SubscribedIamPrincipal"


SubscribedPrincipal: TypeAlias = (
    _SubscribedPrincipal_project
    | _SubscribedPrincipal_user
    | _SubscribedPrincipal_group
    | _SubscribedPrincipal_iam
)


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedPrincipal) -> dict:
    if "project" in value:
        import aws_sdk_datazone.types.subscribed_project

        return {
            "project": aws_sdk_datazone.types.subscribed_project.serialize_json(
                value["project"]
            )
        }
    elif "user" in value:
        import aws_sdk_datazone.types.subscribed_user

        return {
            "user": aws_sdk_datazone.types.subscribed_user.serialize_json(value["user"])
        }
    elif "group" in value:
        import aws_sdk_datazone.types.subscribed_group

        return {
            "group": aws_sdk_datazone.types.subscribed_group.serialize_json(
                value["group"]
            )
        }
    elif "iam" in value:
        import aws_sdk_datazone.types.subscribed_iam_principal

        return {
            "iam": aws_sdk_datazone.types.subscribed_iam_principal.serialize_json(
                value["iam"]
            )
        }
    else:
        raise SerializationError("SubscribedPrincipal: no variant present")


def deserialize_json(data: dict) -> SubscribedPrincipal:
    if "project" in data:
        import aws_sdk_datazone.types.subscribed_project

        return {
            "project": aws_sdk_datazone.types.subscribed_project.deserialize_json(
                data["project"]
            )
        }
    elif "user" in data:
        import aws_sdk_datazone.types.subscribed_user

        return {
            "user": aws_sdk_datazone.types.subscribed_user.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import aws_sdk_datazone.types.subscribed_group

        return {
            "group": aws_sdk_datazone.types.subscribed_group.deserialize_json(
                data["group"]
            )
        }
    elif "iam" in data:
        import aws_sdk_datazone.types.subscribed_iam_principal

        return {
            "iam": aws_sdk_datazone.types.subscribed_iam_principal.deserialize_json(
                data["iam"]
            )
        }
    else:
        raise DeserializationError("SubscribedPrincipal: no recognized variant key")
