"""Generated from Smithy shape ``com.amazonaws.connect#CaseSlaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.field_value_id
    import capo_connect.types.sla_field_value_union_list
    import capo_connect.types.sla_name
    import capo_connect.types.sla_type
    import capo_connect.types.target_sla_minutes


class CaseSlaConfiguration(TypedDict, closed=True):
    name: "capo_connect.types.sla_name.SlaName"
    """<p>Name of an SLA.</p>"""
    type: "capo_connect.types.sla_type.SlaType"
    """<p>Type of SLA for Case SlaAssignmentType.</p>"""
    field_id: NotRequired["capo_connect.types.field_value_id.FieldValueId"]
    """<p>Unique identifier of a Case field.</p>"""
    target_field_values: NotRequired[
        "capo_connect.types.sla_field_value_union_list.SlaFieldValueUnionList"
    ]
    """<p>Represents a list of target field values for the fieldId specified in CaseSlaConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.</p>"""
    target_sla_minutes: "capo_connect.types.target_sla_minutes.TargetSlaMinutes"
    """<p>Target duration in minutes within which an SLA should be completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSlaConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.sla_type

    out["Type"] = capo_connect.types.sla_type.serialize_json(value["type"])
    if "field_id" in value:
        out["FieldId"] = value["field_id"]
    if "target_field_values" in value:
        import capo_connect.types.sla_field_value_union_list

        out["TargetFieldValues"] = (
            capo_connect.types.sla_field_value_union_list.serialize_json(
                value["target_field_values"]
            )
        )
    out["TargetSlaMinutes"] = value["target_sla_minutes"]
    return out


def deserialize_json(data: dict) -> CaseSlaConfiguration:
    out: CaseSlaConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CaseSlaConfiguration.name required")
    if "Type" in data:
        import capo_connect.types.sla_type

        out["type"] = capo_connect.types.sla_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("CaseSlaConfiguration.type required")
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    if "TargetFieldValues" in data:
        import capo_connect.types.sla_field_value_union_list

        out["target_field_values"] = (
            capo_connect.types.sla_field_value_union_list.deserialize_json(
                data["TargetFieldValues"]
            )
        )
    if "TargetSlaMinutes" in data:
        out["target_sla_minutes"] = data["TargetSlaMinutes"]
    else:
        raise DeserializationError("CaseSlaConfiguration.target_sla_minutes required")
    return out
