"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateConnectorV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.provider_update_configuration


class UpdateConnectorV2Request(TypedDict):
    connector_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the connectorV2.</p>"""
    provider: NotRequired[
        "aws_sdk_securityhub.types.provider_update_configuration.ProviderUpdateConfiguration"
    ]
    """<p>The third-party provider’s service configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorV2Request) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "provider" in value:
        import aws_sdk_securityhub.types.provider_update_configuration

        out["Provider"] = (
            aws_sdk_securityhub.types.provider_update_configuration.serialize_json(
                value["provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorV2Request:
    out: UpdateConnectorV2Request = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Provider" in data:
        import aws_sdk_securityhub.types.provider_update_configuration

        out["provider"] = (
            aws_sdk_securityhub.types.provider_update_configuration.deserialize_json(
                data["Provider"]
            )
        )
    return out
