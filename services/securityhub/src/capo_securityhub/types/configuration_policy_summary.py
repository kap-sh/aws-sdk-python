"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class ConfigurationPolicySummary(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the configuration policy. </p>"""
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The universally unique identifier (UUID) of the configuration policy. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The description of the configuration policy. </p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated. </p>"""
    service_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the service that the configuration policy applies to is enabled in the policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicySummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "service_enabled" in value:
        out["ServiceEnabled"] = value["service_enabled"]
    return out


def deserialize_json(data: dict) -> ConfigurationPolicySummary:
    out: ConfigurationPolicySummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdatedAt" in data:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "ServiceEnabled" in data:
        out["service_enabled"] = data["ServiceEnabled"]
    return out
