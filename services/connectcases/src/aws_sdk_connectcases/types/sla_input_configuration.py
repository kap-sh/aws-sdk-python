"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.sla_field_value_union_list
    import aws_sdk_connectcases.types.sla_name
    import aws_sdk_connectcases.types.sla_type
    import aws_sdk_connectcases.types.target_sla_minutes


class SlaInputConfiguration(TypedDict):
    name: "aws_sdk_connectcases.types.sla_name.SlaName"
    """<p>Name of an SLA.</p>"""
    type: "aws_sdk_connectcases.types.sla_type.SlaType"
    """<p>Type of SLA.</p>"""
    field_id: NotRequired["aws_sdk_connectcases.types.field_id.FieldId"]
    """<p>Unique identifier of a field.</p>"""
    target_field_values: NotRequired[
        "aws_sdk_connectcases.types.sla_field_value_union_list.SlaFieldValueUnionList"
    ]
    """<p>Represents a list of target field values for the fieldId specified in SlaInputConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.</p>"""
    target_sla_minutes: "aws_sdk_connectcases.types.target_sla_minutes.TargetSlaMinutes"
    """<p>Target duration in minutes within which an SLA should be completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaInputConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "field_id" in value:
        out["fieldId"] = value["field_id"]
    if "target_field_values" in value:
        import aws_sdk_connectcases.types.sla_field_value_union_list

        out["targetFieldValues"] = (
            aws_sdk_connectcases.types.sla_field_value_union_list.serialize_json(
                value["target_field_values"]
            )
        )
    out["targetSlaMinutes"] = value["target_sla_minutes"]
    return out


def deserialize_json(data: dict) -> SlaInputConfiguration:
    out: SlaInputConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SlaInputConfiguration.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SlaInputConfiguration.type required")
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    if "targetFieldValues" in data:
        import aws_sdk_connectcases.types.sla_field_value_union_list

        out["target_field_values"] = (
            aws_sdk_connectcases.types.sla_field_value_union_list.deserialize_json(
                data["targetFieldValues"]
            )
        )
    if "targetSlaMinutes" in data:
        out["target_sla_minutes"] = data["targetSlaMinutes"]
    else:
        raise DeserializationError("SlaInputConfiguration.target_sla_minutes required")
    return out
