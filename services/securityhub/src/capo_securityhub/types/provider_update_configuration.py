"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.jira_cloud_update_configuration
    import capo_securityhub.types.service_now_update_configuration


class _ProviderUpdateConfiguration_JiraCloud(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_update_configuration.JiraCloudUpdateConfiguration"


class _ProviderUpdateConfiguration_ServiceNow(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_update_configuration.ServiceNowUpdateConfiguration"


ProviderUpdateConfiguration: TypeAlias = (
    _ProviderUpdateConfiguration_JiraCloud | _ProviderUpdateConfiguration_ServiceNow
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderUpdateConfiguration) -> dict:
    if "JiraCloud" in value:
        import capo_securityhub.types.jira_cloud_update_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_update_configuration.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import capo_securityhub.types.service_now_update_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_update_configuration.serialize_json(
                value["ServiceNow"]
            )
        }
    else:
        raise SerializationError("ProviderUpdateConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderUpdateConfiguration:
    if "JiraCloud" in data:
        import capo_securityhub.types.jira_cloud_update_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_update_configuration.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif "ServiceNow" in data:
        import capo_securityhub.types.service_now_update_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_update_configuration.deserialize_json(
                data["ServiceNow"]
            )
        }
    else:
        raise DeserializationError(
            "ProviderUpdateConfiguration: no recognized variant key"
        )
