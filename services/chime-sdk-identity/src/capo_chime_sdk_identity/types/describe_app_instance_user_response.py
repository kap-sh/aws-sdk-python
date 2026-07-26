"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user


class DescribeAppInstanceUserResponse(TypedDict, closed=True):
    app_instance_user: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_user.AppInstanceUser"
    ]
    """<p>The name of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "app_instance_user" in value:
        import capo_chime_sdk_identity.types.app_instance_user

        out["AppInstanceUser"] = (
            capo_chime_sdk_identity.types.app_instance_user.serialize_json(
                value["app_instance_user"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserResponse:
    out: DescribeAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUser" in data:
        import capo_chime_sdk_identity.types.app_instance_user

        out["app_instance_user"] = (
            capo_chime_sdk_identity.types.app_instance_user.deserialize_json(
                data["AppInstanceUser"]
            )
        )
    return out
