"""Generated from Smithy shape ``com.amazonaws.ecr#DeleteSigningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_id
    import capo_ecr.types.signing_configuration


class DeleteSigningConfigurationResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry.</p>"""
    signing_configuration: NotRequired[
        "capo_ecr.types.signing_configuration.SigningConfiguration"
    ]
    """<p>The registry's deleted signing configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSigningConfigurationResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "signing_configuration" in value:
        import capo_ecr.types.signing_configuration

        out["signingConfiguration"] = (
            capo_ecr.types.signing_configuration.serialize_aws_json_1_1(
                value["signing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSigningConfigurationResponse:
    out: DeleteSigningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("signingConfiguration") is not None:
        import capo_ecr.types.signing_configuration

        out["signing_configuration"] = (
            capo_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    return out
