"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeServiceIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_integration_config


class DescribeServiceIntegrationResponse(TypedDict):
    service_integration: NotRequired[
        "aws_sdk_devops_guru.types.service_integration_config.ServiceIntegrationConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeServiceIntegrationResponse) -> dict:
    out: dict = {}
    if "service_integration" in value:
        import aws_sdk_devops_guru.types.service_integration_config

        out["ServiceIntegration"] = (
            aws_sdk_devops_guru.types.service_integration_config.serialize_json(
                value["service_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeServiceIntegrationResponse:
    out: DescribeServiceIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "ServiceIntegration" in data:
        import aws_sdk_devops_guru.types.service_integration_config

        out["service_integration"] = (
            aws_sdk_devops_guru.types.service_integration_config.deserialize_json(
                data["ServiceIntegration"]
            )
        )
    return out
