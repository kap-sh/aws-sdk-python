"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateServiceIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.update_service_integration_config


class UpdateServiceIntegrationRequest(TypedDict):
    service_integration: "aws_sdk_devops_guru.types.update_service_integration_config.UpdateServiceIntegrationConfig"
    """<p> An <code>IntegratedServiceConfig</code> object used to specify the integrated service you want to update, and whether you want to update it to enabled or disabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceIntegrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.update_service_integration_config

    out["ServiceIntegration"] = (
        aws_sdk_devops_guru.types.update_service_integration_config.serialize_json(
            value["service_integration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceIntegrationRequest:
    out: UpdateServiceIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "ServiceIntegration" in data:
        import aws_sdk_devops_guru.types.update_service_integration_config

        out["service_integration"] = (
            aws_sdk_devops_guru.types.update_service_integration_config.deserialize_json(
                data["ServiceIntegration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceIntegrationRequest.service_integration required"
        )
    return out
