"""Generated from Smithy shape ``com.amazonaws.ecr#PutSigningConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_configuration


class PutSigningConfigurationResponse(TypedDict):
    signing_configuration: NotRequired[
        "aws_sdk_ecr.types.signing_configuration.SigningConfiguration"
    ]
    """<p>The registry's updated signing configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSigningConfigurationResponse) -> dict:
    out: dict = {}
    if "signing_configuration" in value:
        import aws_sdk_ecr.types.signing_configuration

        out["signingConfiguration"] = (
            aws_sdk_ecr.types.signing_configuration.serialize_aws_json_1_1(
                value["signing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSigningConfigurationResponse:
    out: PutSigningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "signingConfiguration" in data:
        import aws_sdk_ecr.types.signing_configuration

        out["signing_configuration"] = (
            aws_sdk_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    return out
