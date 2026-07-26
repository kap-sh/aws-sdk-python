"""Generated from Smithy shape ``com.amazonaws.batch#ServiceResourceId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.service_resource_id_name
    import capo_batch.types.string


class ServiceResourceId(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.service_resource_id_name.ServiceResourceIdName"]
    """<p>The name of the resource identifier. </p>"""
    value: NotRequired["capo_batch.types.string.String"]
    """<p>The value of the resource identifier. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceId) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_batch.types.service_resource_id_name

        out["name"] = capo_batch.types.service_resource_id_name.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ServiceResourceId:
    out: ServiceResourceId = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_batch.types.service_resource_id_name

        out["name"] = capo_batch.types.service_resource_id_name.deserialize_json(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
