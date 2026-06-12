"""Generated from Smithy shape ``com.amazonaws.ecr#PutSigningConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_configuration


class PutSigningConfigurationRequest(TypedDict):
    signing_configuration: (
        "aws_sdk_ecr.types.signing_configuration.SigningConfiguration"
    )
    """<p>The signing configuration to assign to the registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutSigningConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_ecr.types.signing_configuration

    out["signingConfiguration"] = (
        aws_sdk_ecr.types.signing_configuration.serialize_aws_json_1_1(
            value["signing_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutSigningConfigurationRequest:
    out: PutSigningConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "signingConfiguration" in data:
        import aws_sdk_ecr.types.signing_configuration

        out["signing_configuration"] = (
            aws_sdk_ecr.types.signing_configuration.deserialize_aws_json_1_1(
                data["signingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutSigningConfigurationRequest.signing_configuration required"
        )
    return out
