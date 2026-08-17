"""Generated from Smithy shape ``com.amazonaws.ecr#PutRegistryScanningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_scanning_configuration


class PutRegistryScanningConfigurationResponse(TypedDict, closed=True):
    registry_scanning_configuration: NotRequired[
        "capo_ecr.types.registry_scanning_configuration.RegistryScanningConfiguration"
    ]
    """<p>The scanning configuration for your registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryScanningConfigurationResponse) -> dict:
    out: dict = {}
    if "registry_scanning_configuration" in value:
        import capo_ecr.types.registry_scanning_configuration

        out["registryScanningConfiguration"] = (
            capo_ecr.types.registry_scanning_configuration.serialize_aws_json_1_1(
                value["registry_scanning_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryScanningConfigurationResponse:
    out: PutRegistryScanningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryScanningConfiguration") is not None:
        import capo_ecr.types.registry_scanning_configuration

        out["registry_scanning_configuration"] = (
            capo_ecr.types.registry_scanning_configuration.deserialize_aws_json_1_1(
                data["registryScanningConfiguration"]
            )
        )
    return out
