"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateManagedThingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.created_at
    import aws_sdk_iot_managed_integrations.types.managed_thing_arn
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class CreateManagedThingResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the managed thing.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_arn.ManagedThingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the managed thing.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the device creation request occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateManagedThingResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateManagedThingResponse:
    out: CreateManagedThingResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
