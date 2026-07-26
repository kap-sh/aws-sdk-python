"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EventReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.generated_id


class _EventReference_resource(TypedDict, closed=True):
    resource: "capo_ssm_incidents.types.arn.Arn"


class _EventReference_relatedItemId(TypedDict, closed=True):
    relatedItemId: "capo_ssm_incidents.types.generated_id.GeneratedId"


EventReference: TypeAlias = _EventReference_resource | _EventReference_relatedItemId


# --- restJson1 ser/de ---
def serialize_json(value: EventReference) -> dict:
    if "resource" in value:
        return {"resource": value["resource"]}
    elif "relatedItemId" in value:
        return {"relatedItemId": value["relatedItemId"]}
    else:
        raise SerializationError("EventReference: no variant present")


def deserialize_json(data: dict) -> EventReference:
    if "resource" in data:
        return {"resource": data["resource"]}
    elif "relatedItemId" in data:
        return {"relatedItemId": data["relatedItemId"]}
    else:
        raise DeserializationError("EventReference: no recognized variant key")
