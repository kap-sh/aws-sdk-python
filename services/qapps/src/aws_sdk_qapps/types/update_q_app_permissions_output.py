"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppPermissionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qapps.types.permissions_output_list


class UpdateQAppPermissionsOutput(TypedDict):
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q App for which permissions were updated.</p>"""
    app_id: NotRequired["str"]
    """<p>The unique identifier of the Amazon Q App for which permissions were updated.</p>"""
    permissions: NotRequired[
        "aws_sdk_qapps.types.permissions_output_list.PermissionsOutputList"
    ]
    """<p>The updated list of permissions for the Amazon Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppPermissionsOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "permissions" in value:
        import aws_sdk_qapps.types.permissions_output_list

        out["permissions"] = aws_sdk_qapps.types.permissions_output_list.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppPermissionsOutput:
    out: UpdateQAppPermissionsOutput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "permissions" in data:
        import aws_sdk_qapps.types.permissions_output_list

        out["permissions"] = (
            aws_sdk_qapps.types.permissions_output_list.deserialize_json(
                data["permissions"]
            )
        )
    return out
