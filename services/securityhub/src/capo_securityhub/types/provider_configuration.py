"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securityhub.types.jira_cloud_provider_configuration
    import capo_securityhub.types.service_now_provider_configuration


class _ProviderConfiguration_JiraCloud(TypedDict, closed=True):
    JiraCloud: "capo_securityhub.types.jira_cloud_provider_configuration.JiraCloudProviderConfiguration"


class _ProviderConfiguration_ServiceNow(TypedDict, closed=True):
    ServiceNow: "capo_securityhub.types.service_now_provider_configuration.ServiceNowProviderConfiguration"


ProviderConfiguration: TypeAlias = (
    _ProviderConfiguration_JiraCloud | _ProviderConfiguration_ServiceNow
)


# --- restJson1 ser/de ---
def serialize_json(value: ProviderConfiguration) -> dict:
    if "JiraCloud" in value:
        import capo_securityhub.types.jira_cloud_provider_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_provider_configuration.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import capo_securityhub.types.service_now_provider_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_provider_configuration.serialize_json(
                value["ServiceNow"]
            )
        }
    else:
        raise SerializationError("ProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> ProviderConfiguration:
    if "JiraCloud" in data:
        import capo_securityhub.types.jira_cloud_provider_configuration

        return {
            "JiraCloud": capo_securityhub.types.jira_cloud_provider_configuration.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif "ServiceNow" in data:
        import capo_securityhub.types.service_now_provider_configuration

        return {
            "ServiceNow": capo_securityhub.types.service_now_provider_configuration.deserialize_json(
                data["ServiceNow"]
            )
        }
    else:
        raise DeserializationError("ProviderConfiguration: no recognized variant key")
