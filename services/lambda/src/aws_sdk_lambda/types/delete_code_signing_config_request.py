"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config_arn


class DeleteCodeSigningConfigRequest(TypedDict):
    code_signing_config_arn: (
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSigningConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCodeSigningConfigRequest:
    out: DeleteCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    return out
