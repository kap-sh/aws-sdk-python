"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceAdminResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_admin


class DescribeAppInstanceAdminResponse(TypedDict):
    app_instance_admin: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_admin.AppInstanceAdmin"
    ]
    """<p>The ARN and name of the <code>AppInstanceUser</code>, the ARN of the <code>AppInstance</code>, and the created and last-updated timestamps. All timestamps use epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceAdminResponse) -> dict:
    out: dict = {}
    if "app_instance_admin" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_admin

        out["AppInstanceAdmin"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_admin.serialize_json(
                value["app_instance_admin"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceAdminResponse:
    out: DescribeAppInstanceAdminResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceAdmin" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_admin

        out["app_instance_admin"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_admin.deserialize_json(
                data["AppInstanceAdmin"]
            )
        )
    return out
