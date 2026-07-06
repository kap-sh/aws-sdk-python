"""Generated from Smithy shape ``com.amazonaws.ecr#GetRegistryScanningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.registry_scanning_configuration


class GetRegistryScanningConfigurationResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    scanning_configuration: NotRequired[
        "aws_sdk_ecr.types.registry_scanning_configuration.RegistryScanningConfiguration"
    ]
    """<p>The scanning configuration for the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegistryScanningConfigurationResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "scanning_configuration" in value:
        import aws_sdk_ecr.types.registry_scanning_configuration

        out["scanningConfiguration"] = (
            aws_sdk_ecr.types.registry_scanning_configuration.serialize_aws_json_1_1(
                value["scanning_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegistryScanningConfigurationResponse:
    out: GetRegistryScanningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "scanningConfiguration" in data:
        import aws_sdk_ecr.types.registry_scanning_configuration

        out["scanning_configuration"] = (
            aws_sdk_ecr.types.registry_scanning_configuration.deserialize_aws_json_1_1(
                data["scanningConfiguration"]
            )
        )
    return out
