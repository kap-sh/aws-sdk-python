"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCodeSigningConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config


class CreateCodeSigningConfigResponse(TypedDict):
    code_signing_config: "aws_sdk_lambda.types.code_signing_config.CodeSigningConfig"
    """<p>The code signing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSigningConfigResponse) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.code_signing_config

    out["CodeSigningConfig"] = aws_sdk_lambda.types.code_signing_config.serialize_json(
        value["code_signing_config"]
    )
    return out


def deserialize_json(data: dict) -> CreateCodeSigningConfigResponse:
    out: CreateCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    if "CodeSigningConfig" in data:
        import aws_sdk_lambda.types.code_signing_config

        out["code_signing_config"] = (
            aws_sdk_lambda.types.code_signing_config.deserialize_json(
                data["CodeSigningConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeSigningConfigResponse.code_signing_config required"
        )
    return out
