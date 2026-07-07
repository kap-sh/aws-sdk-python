"""Generated from Smithy shape ``com.amazonaws.lambda#GetCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config_arn


class GetCodeSigningConfigRequest(TypedDict, closed=True):
    code_signing_config_arn: (
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSigningConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeSigningConfigRequest:
    out: GetCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    return out
