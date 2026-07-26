"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingMetaDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.meta_data


class GetManagedThingMetaDataResponse(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The managed thing id.</p>"""
    meta_data: NotRequired["capo_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingMetaDataResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "meta_data" in value:
        import capo_iot_managed_integrations.types.meta_data

        out["MetaData"] = capo_iot_managed_integrations.types.meta_data.serialize_json(
            value["meta_data"]
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingMetaDataResponse:
    out: GetManagedThingMetaDataResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "MetaData" in data:
        import capo_iot_managed_integrations.types.meta_data

        out["meta_data"] = (
            capo_iot_managed_integrations.types.meta_data.deserialize_json(
                data["MetaData"]
            )
        )
    return out
