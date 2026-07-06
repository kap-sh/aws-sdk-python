"""Generated from Smithy shape ``com.amazonaws.connect#AssignSlaActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.case_sla_configuration
    import aws_sdk_connect.types.sla_assignment_type


class AssignSlaActionDefinition(TypedDict, closed=True):
    sla_assignment_type: "aws_sdk_connect.types.sla_assignment_type.SlaAssignmentType"
    """<p>Type of SLA assignment.</p>"""
    case_sla_configuration: NotRequired[
        "aws_sdk_connect.types.case_sla_configuration.CaseSlaConfiguration"
    ]
    """<p>The SLA configuration for Case SLA Assignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignSlaActionDefinition) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.sla_assignment_type

    out["SlaAssignmentType"] = aws_sdk_connect.types.sla_assignment_type.serialize_json(
        value["sla_assignment_type"]
    )
    if "case_sla_configuration" in value:
        import aws_sdk_connect.types.case_sla_configuration

        out["CaseSlaConfiguration"] = (
            aws_sdk_connect.types.case_sla_configuration.serialize_json(
                value["case_sla_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssignSlaActionDefinition:
    out: AssignSlaActionDefinition = {}  # type: ignore[typeddict-item]
    if "SlaAssignmentType" in data:
        import aws_sdk_connect.types.sla_assignment_type

        out["sla_assignment_type"] = (
            aws_sdk_connect.types.sla_assignment_type.deserialize_json(
                data["SlaAssignmentType"]
            )
        )
    else:
        raise DeserializationError(
            "AssignSlaActionDefinition.sla_assignment_type required"
        )
    if "CaseSlaConfiguration" in data:
        import aws_sdk_connect.types.case_sla_configuration

        out["case_sla_configuration"] = (
            aws_sdk_connect.types.case_sla_configuration.deserialize_json(
                data["CaseSlaConfiguration"]
            )
        )
    return out
