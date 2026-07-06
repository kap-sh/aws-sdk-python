"""Generated from Smithy shape ``com.amazonaws.securityhub#ProviderDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securityhub.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.jira_cloud_detail
    import aws_sdk_securityhub.types.service_now_detail


class _ProviderDetail_JiraCloud(TypedDict, closed=True):
    JiraCloud: "aws_sdk_securityhub.types.jira_cloud_detail.JiraCloudDetail"


class _ProviderDetail_ServiceNow(TypedDict, closed=True):
    ServiceNow: "aws_sdk_securityhub.types.service_now_detail.ServiceNowDetail"


ProviderDetail: TypeAlias = _ProviderDetail_JiraCloud | _ProviderDetail_ServiceNow


# --- restJson1 ser/de ---
def serialize_json(value: ProviderDetail) -> dict:
    if "JiraCloud" in value:
        import aws_sdk_securityhub.types.jira_cloud_detail

        return {
            "JiraCloud": aws_sdk_securityhub.types.jira_cloud_detail.serialize_json(
                value["JiraCloud"]
            )
        }
    elif "ServiceNow" in value:
        import aws_sdk_securityhub.types.service_now_detail

        return {
            "ServiceNow": aws_sdk_securityhub.types.service_now_detail.serialize_json(
                value["ServiceNow"]
            )
        }
    else:
        raise SerializationError("ProviderDetail: no variant present")


def deserialize_json(data: dict) -> ProviderDetail:
    if "JiraCloud" in data:
        import aws_sdk_securityhub.types.jira_cloud_detail

        return {
            "JiraCloud": aws_sdk_securityhub.types.jira_cloud_detail.deserialize_json(
                data["JiraCloud"]
            )
        }
    elif "ServiceNow" in data:
        import aws_sdk_securityhub.types.service_now_detail

        return {
            "ServiceNow": aws_sdk_securityhub.types.service_now_detail.deserialize_json(
                data["ServiceNow"]
            )
        }
    else:
        raise DeserializationError("ProviderDetail: no recognized variant key")
