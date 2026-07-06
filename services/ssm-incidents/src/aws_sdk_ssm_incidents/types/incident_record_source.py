"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecordSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.incident_source
    import aws_sdk_ssm_incidents.types.service_principal


class IncidentRecordSource(TypedDict, closed=True):
    created_by: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The principal that started the incident.</p>"""
    invoked_by: NotRequired[
        "aws_sdk_ssm_incidents.types.service_principal.ServicePrincipal"
    ]
    """<p>The service principal that assumed the role specified in <code>createdBy</code>. If no service principal assumed the role this will be left blank.</p>"""
    resource_arn: NotRequired["aws_sdk_ssm_incidents.types.arn.Arn"]
    """<p>The resource that caused the incident to be created.</p>"""
    source: "aws_sdk_ssm_incidents.types.incident_source.IncidentSource"
    """<p>The service that started the incident. This can be manually created from Incident Manager, automatically created using an Amazon CloudWatch alarm, or Amazon EventBridge event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecordSource) -> dict:
    out: dict = {}
    out["createdBy"] = value["created_by"]
    if "invoked_by" in value:
        out["invokedBy"] = value["invoked_by"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> IncidentRecordSource:
    out: IncidentRecordSource = {}  # type: ignore[typeddict-item]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("IncidentRecordSource.created_by required")
    if "invokedBy" in data:
        out["invoked_by"] = data["invokedBy"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("IncidentRecordSource.source required")
    return out
