"""Generated from Smithy shape ``com.amazonaws.ecr#PutSigningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.signing_configuration


class PutSigningConfigurationResponse(TypedDict, closed=True):
    signing_configuration: NotRequired[
        "capo_ecr.types.signing_configuration.SigningConfiguration"
    ]
    """<p>The registry's updated signing configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSigningConfigurationResponse) -> dict:
    out: dict = {}
    if "signing_configuration" in value:
        import capo_ecr.types.signing_configuration

        out["signingConfiguration"] = (
            capo_ecr.types.signing_configuration.serialize_aws_json_1_1(
                value["signing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSigningConfigurationResponse:
    out: PutSigningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("signingConfiguration") is not None:
        import capo_ecr.types.signing_configuration

        out["signing_configuration"] = (
            capo_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    return out
