"""Generated from Smithy shape ``com.amazonaws.securityhub#ServiceNowProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ServiceNowProviderConfiguration(TypedDict, closed=True):
    instance_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instance name of ServiceNow ITSM.</p>"""
    secret_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the ServiceNow credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowProviderConfiguration) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["InstanceName"] = value["instance_name"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> ServiceNowProviderConfiguration:
    out: ServiceNowProviderConfiguration = {}  # type: ignore[typeddict-item]
    if "InstanceName" in data:
        out["instance_name"] = data["InstanceName"]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
