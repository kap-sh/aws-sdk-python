"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.metric_definition
    import aws_sdk_ssm_incidents.types.pager_duty_incident_detail
    import aws_sdk_ssm_incidents.types.url


class _ItemValue_arn(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"


class _ItemValue_url(TypedDict):
    url: "aws_sdk_ssm_incidents.types.url.Url"


class _ItemValue_metricDefinition(TypedDict):
    metricDefinition: "aws_sdk_ssm_incidents.types.metric_definition.MetricDefinition"


class _ItemValue_pagerDutyIncidentDetail(TypedDict):
    pagerDutyIncidentDetail: (
        "aws_sdk_ssm_incidents.types.pager_duty_incident_detail.PagerDutyIncidentDetail"
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
        import aws_sdk_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": aws_sdk_ssm_incidents.types.pager_duty_incident_detail.serialize_json(
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
        import aws_sdk_ssm_incidents.types.pager_duty_incident_detail

        return {
            "pagerDutyIncidentDetail": aws_sdk_ssm_incidents.types.pager_duty_incident_detail.deserialize_json(
                data["pagerDutyIncidentDetail"]
            )
        }
    else:
        raise DeserializationError("ItemValue: no recognized variant key")
