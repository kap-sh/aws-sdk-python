"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicApiKeyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.api_key_value
    import aws_sdk_devops_agent.types.new_relic_alert_policy_ids
    import aws_sdk_devops_agent.types.new_relic_application_ids
    import aws_sdk_devops_agent.types.new_relic_entity_guids
    import aws_sdk_devops_agent.types.new_relic_region


class NewRelicApiKeyConfig(TypedDict):
    api_key: "aws_sdk_devops_agent.types.api_key_value.ApiKeyValue"
    """<p>New Relic User API Key</p>"""
    account_id: "str"
    """<p>New Relic Account ID</p>"""
    region: "aws_sdk_devops_agent.types.new_relic_region.NewRelicRegion"
    """<p>New Relic region (US or EU)</p>"""
    application_ids: NotRequired[
        "aws_sdk_devops_agent.types.new_relic_application_ids.NewRelicApplicationIds"
    ]
    """<p>List of monitored APM application IDs in New Relic</p>"""
    entity_guids: NotRequired[
        "aws_sdk_devops_agent.types.new_relic_entity_guids.NewRelicEntityGuids"
    ]
    """<p>List of globally unique IDs for New Relic resources (apps, hosts, services)</p>"""
    alert_policy_ids: NotRequired[
        "aws_sdk_devops_agent.types.new_relic_alert_policy_ids.NewRelicAlertPolicyIds"
    ]
    """<p>List of alert policy IDs grouping related conditions</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicApiKeyConfig) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    out["accountId"] = value["account_id"]
    import aws_sdk_devops_agent.types.new_relic_region

    out["region"] = aws_sdk_devops_agent.types.new_relic_region.serialize_json(
        value["region"]
    )
    if "application_ids" in value:
        import aws_sdk_devops_agent.types.new_relic_application_ids

        out["applicationIds"] = (
            aws_sdk_devops_agent.types.new_relic_application_ids.serialize_json(
                value["application_ids"]
            )
        )
    if "entity_guids" in value:
        import aws_sdk_devops_agent.types.new_relic_entity_guids

        out["entityGuids"] = (
            aws_sdk_devops_agent.types.new_relic_entity_guids.serialize_json(
                value["entity_guids"]
            )
        )
    if "alert_policy_ids" in value:
        import aws_sdk_devops_agent.types.new_relic_alert_policy_ids

        out["alertPolicyIds"] = (
            aws_sdk_devops_agent.types.new_relic_alert_policy_ids.serialize_json(
                value["alert_policy_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> NewRelicApiKeyConfig:
    out: NewRelicApiKeyConfig = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("NewRelicApiKeyConfig.api_key required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("NewRelicApiKeyConfig.account_id required")
    if "region" in data:
        import aws_sdk_devops_agent.types.new_relic_region

        out["region"] = aws_sdk_devops_agent.types.new_relic_region.deserialize_json(
            data["region"]
        )
    else:
        raise DeserializationError("NewRelicApiKeyConfig.region required")
    if "applicationIds" in data:
        import aws_sdk_devops_agent.types.new_relic_application_ids

        out["application_ids"] = (
            aws_sdk_devops_agent.types.new_relic_application_ids.deserialize_json(
                data["applicationIds"]
            )
        )
    if "entityGuids" in data:
        import aws_sdk_devops_agent.types.new_relic_entity_guids

        out["entity_guids"] = (
            aws_sdk_devops_agent.types.new_relic_entity_guids.deserialize_json(
                data["entityGuids"]
            )
        )
    if "alertPolicyIds" in data:
        import aws_sdk_devops_agent.types.new_relic_alert_policy_ids

        out["alert_policy_ids"] = (
            aws_sdk_devops_agent.types.new_relic_alert_policy_ids.deserialize_json(
                data["alertPolicyIds"]
            )
        )
    return out
