"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PagerDutyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.pager_duty_incident_configuration


class PagerDutyConfiguration(TypedDict):
    name: "str"
    """<p>The name of the PagerDuty configuration.</p>"""
    secret_id: "str"
    """<p>The ID of the Amazon Web Services Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.</p>"""
    pager_duty_incident_configuration: "aws_sdk_ssm_incidents.types.pager_duty_incident_configuration.PagerDutyIncidentConfiguration"
    """<p>Details about the PagerDuty service associated with the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["secretId"] = value["secret_id"]
    import aws_sdk_ssm_incidents.types.pager_duty_incident_configuration

    out["pagerDutyIncidentConfiguration"] = (
        aws_sdk_ssm_incidents.types.pager_duty_incident_configuration.serialize_json(
            value["pager_duty_incident_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PagerDutyConfiguration:
    out: PagerDutyConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PagerDutyConfiguration.name required")
    if "secretId" in data:
        out["secret_id"] = data["secretId"]
    else:
        raise DeserializationError("PagerDutyConfiguration.secret_id required")
    if "pagerDutyIncidentConfiguration" in data:
        import aws_sdk_ssm_incidents.types.pager_duty_incident_configuration

        out["pager_duty_incident_configuration"] = (
            aws_sdk_ssm_incidents.types.pager_duty_incident_configuration.deserialize_json(
                data["pagerDutyIncidentConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PagerDutyConfiguration.pager_duty_incident_configuration required"
        )
    return out
