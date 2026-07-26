"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.metric_definition
    import capo_ssm_incidents.types.pager_duty_incident_detail
    import capo_ssm_incidents.types.url


class _ItemValue_arn(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"


class _ItemValue_url(TypedDict, closed=True):
    url: "capo_ssm_incidents.types.url.Url"


class _ItemValue_metricDefinition(TypedDict, closed=True):
    metricDefinition: "capo_ssm_incidents.types.metric_definition.MetricDefinition"


class _ItemValue_pagerDutyIncidentDetail(TypedDict, closed=True):
    pagerDutyIncidentDetail: (
        "capo_ssm_incidents.types.pager_duty_incident_detail.PagerDutyIncidentDetail"
    )


ItemValue: TypeAlias = (
    _ItemValue_arn
    | _ItemValue_url
    | _ItemValue_metricDefinition
    | _ItemValue_pagerDutyIncidentDetail
)


# --- restJson1 ser/de ---
def serialize_json(value: ItemValue) -> dict:
    if "arn" in value:
        return {"arn": value["arn"]}
    elif "url" in value:
        return {"url": value["url"]}
    elif "metricDefinition" in value:
        return {"metricDefinition": value["metricDefinition"]}
    elif "pagerDutyIncidentDetail" in value:
        import capo_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": capo_ssm_incidents.types.pager_duty_incident_detail.serialize_json(
                value["pagerDutyIncidentDetail"]
            )
        }
    else:
        raise SerializationError("ItemValue: no variant present")


def deserialize_json(data: dict) -> ItemValue:
    if "arn" in data:
        return {"arn": data["arn"]}
    elif "url" in data:
        return {"url": data["url"]}
    elif "metricDefinition" in data:
        return {"metricDefinition": data["metricDefinition"]}
    elif "pagerDutyIncidentDetail" in data:
        import capo_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": capo_ssm_incidents.types.pager_duty_incident_detail.deserialize_json(
                data["pagerDutyIncidentDetail"]
            )
        }
    else:
        raise DeserializationError("ItemValue: no recognized variant key")
