"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#InstanceIdFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.instance_id_filter_operator


class InstanceIdFilter(TypedDict):
    value: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    operator: "aws_sdk_connectcampaignsv2.types.instance_id_filter_operator.InstanceIdFilterOperator"


# --- restJson1 ser/de ---
def serialize_json(value: InstanceIdFilter) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> InstanceIdFilter:
    out: InstanceIdFilter = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("InstanceIdFilter.value required")
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("InstanceIdFilter.operator required")
    return out
