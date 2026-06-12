"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.sla_completion_time
    import aws_sdk_connectcases.types.sla_field_value_union_list
    import aws_sdk_connectcases.types.sla_name
    import aws_sdk_connectcases.types.sla_status
    import aws_sdk_connectcases.types.sla_target_time
    import aws_sdk_connectcases.types.sla_type


class SlaConfiguration(TypedDict):
    name: "aws_sdk_connectcases.types.sla_name.SlaName"
    """<p>Name of an SLA.</p>"""
    type: "aws_sdk_connectcases.types.sla_type.SlaType"
    """<p>Type of SLA.</p>"""
    status: "aws_sdk_connectcases.types.sla_status.SlaStatus"
    """<p>Status of an SLA.</p>"""
    field_id: NotRequired["aws_sdk_connectcases.types.field_id.FieldId"]
    """<p>Unique identifier of a field.</p>"""
    target_field_values: NotRequired[
        "aws_sdk_connectcases.types.sla_field_value_union_list.SlaFieldValueUnionList"
    ]
    """<p>Represents a list of target field values for the fieldId specified in SlaConfiguration.</p>"""
    target_time: "aws_sdk_connectcases.types.sla_target_time.SlaTargetTime"
    """<p>Target time by which an SLA should be completed.</p>"""
    completion_time: NotRequired[
        "aws_sdk_connectcases.types.sla_completion_time.SlaCompletionTime"
    ]
    """<p>Time at which an SLA was completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlaConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    if "field_id" in value:
        out["fieldId"] = value["field_id"]
    if "target_field_values" in value:
        import aws_sdk_connectcases.types.sla_field_value_union_list

        out["targetFieldValues"] = (
            aws_sdk_connectcases.types.sla_field_value_union_list.serialize_json(
                value["target_field_values"]
            )
        )
    import aws_sdk_connectcases.types.sla_target_time

    out["targetTime"] = aws_sdk_connectcases.types.sla_target_time.serialize_json(
        value["target_time"]
    )
    if "completion_time" in value:
        import aws_sdk_connectcases.types.sla_completion_time

        out["completionTime"] = (
            aws_sdk_connectcases.types.sla_completion_time.serialize_json(
                value["completion_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> SlaConfiguration:
    out: SlaConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SlaConfiguration.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SlaConfiguration.type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SlaConfiguration.status required")
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    if "targetFieldValues" in data:
        import aws_sdk_connectcases.types.sla_field_value_union_list

        out["target_field_values"] = (
            aws_sdk_connectcases.types.sla_field_value_union_list.deserialize_json(
                data["targetFieldValues"]
            )
        )
    if "targetTime" in data:
        import aws_sdk_connectcases.types.sla_target_time

        out["target_time"] = (
            aws_sdk_connectcases.types.sla_target_time.deserialize_json(
                data["targetTime"]
            )
        )
    else:
        raise DeserializationError("SlaConfiguration.target_time required")
    if "completionTime" in data:
        import aws_sdk_connectcases.types.sla_completion_time

        out["completion_time"] = (
            aws_sdk_connectcases.types.sla_completion_time.deserialize_json(
                data["completionTime"]
            )
        )
    return out
