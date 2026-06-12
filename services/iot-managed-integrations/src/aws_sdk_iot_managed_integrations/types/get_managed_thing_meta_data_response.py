"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingMetaDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.meta_data


class GetManagedThingMetaDataResponse(TypedDict):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The managed thing id.</p>"""
    meta_data: NotRequired["aws_sdk_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingMetaDataResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "meta_data" in value:
        import aws_sdk_iot_managed_integrations.types.meta_data

        out["MetaData"] = (
            aws_sdk_iot_managed_integrations.types.meta_data.serialize_json(
                value["meta_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingMetaDataResponse:
    out: GetManagedThingMetaDataResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "MetaData" in data:
        import aws_sdk_iot_managed_integrations.types.meta_data

        out["meta_data"] = (
            aws_sdk_iot_managed_integrations.types.meta_data.deserialize_json(
                data["MetaData"]
            )
        )
    return out
