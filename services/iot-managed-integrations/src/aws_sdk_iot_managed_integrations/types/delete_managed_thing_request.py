"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteManagedThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class DeleteManagedThingRequest(TypedDict):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The id of the managed thing.</p>"""
    force: NotRequired["bool"]
    """<p>When set to <code>TRUE</code>, a forceful deteletion of the managed thing will occur. When set to <code>FALSE</code>, a non-forceful deletion of the managed thing will occur.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteManagedThingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteManagedThingRequest:
    out: DeleteManagedThingRequest = {}  # type: ignore[typeddict-item]
    return out
