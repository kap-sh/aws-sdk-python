"""Generated from Smithy shape ``com.amazonaws.ecr#GetSigningConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.signing_configuration


class GetSigningConfigurationResponse(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry.</p>"""
    signing_configuration: NotRequired[
        "aws_sdk_ecr.types.signing_configuration.SigningConfiguration"
    ]
    """<p>The registry's signing configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSigningConfigurationResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "signing_configuration" in value:
        import aws_sdk_ecr.types.signing_configuration

        out["signingConfiguration"] = (
            aws_sdk_ecr.types.signing_configuration.serialize_aws_json_1_1(
                value["signing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSigningConfigurationResponse:
    out: GetSigningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "signingConfiguration" in data:
        import aws_sdk_ecr.types.signing_configuration

        out["signing_configuration"] = (
            aws_sdk_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    return out
