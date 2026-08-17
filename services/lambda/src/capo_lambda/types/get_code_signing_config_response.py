"""Generated from Smithy shape ``com.amazonaws.lambda#GetCodeSigningConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.code_signing_config


class GetCodeSigningConfigResponse(TypedDict, closed=True):
    code_signing_config: "capo_lambda.types.code_signing_config.CodeSigningConfig"
    """<p>The code signing configuration</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSigningConfigResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.code_signing_config

    out["CodeSigningConfig"] = capo_lambda.types.code_signing_config.serialize_json(
        value["code_signing_config"]
    )
    return out


def deserialize_json(data: dict) -> GetCodeSigningConfigResponse:
    out: GetCodeSigningConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("CodeSigningConfig") is not None:
        import capo_lambda.types.code_signing_config

        out["code_signing_config"] = (
            capo_lambda.types.code_signing_config.deserialize_json(
                data["CodeSigningConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeSigningConfigResponse.code_signing_config required"
        )
    return out
