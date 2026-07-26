"""Generated from Smithy shape ``com.amazonaws.ecr#PutSigningConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.signing_configuration


class PutSigningConfigurationRequest(TypedDict, closed=True):
    signing_configuration: "capo_ecr.types.signing_configuration.SigningConfiguration"
    """<p>The signing configuration to assign to the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSigningConfigurationRequest) -> dict:
    out: dict = {}
    import capo_ecr.types.signing_configuration

    out["signingConfiguration"] = (
        capo_ecr.types.signing_configuration.serialize_aws_json_1_1(
            value["signing_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSigningConfigurationRequest:
    out: PutSigningConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "signingConfiguration" in data:
        import capo_ecr.types.signing_configuration

        out["signing_configuration"] = (
            capo_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutSigningConfigurationRequest.signing_configuration required"
        )
    return out
