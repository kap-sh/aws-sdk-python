"""Generated from Smithy shape ``com.amazonaws.lambda#ListCodeSigningConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.code_signing_config_list
    import aws_sdk_lambda.types.string


class ListCodeSigningConfigsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    code_signing_configs: NotRequired[
        "aws_sdk_lambda.types.code_signing_config_list.CodeSigningConfigList"
    ]
    """<p>The code signing configurations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSigningConfigsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "code_signing_configs" in value:
        import aws_sdk_lambda.types.code_signing_config_list

        out["CodeSigningConfigs"] = (
            aws_sdk_lambda.types.code_signing_config_list.serialize_json(
                value["code_signing_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCodeSigningConfigsResponse:
    out: ListCodeSigningConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "CodeSigningConfigs" in data:
        import aws_sdk_lambda.types.code_signing_config_list

        out["code_signing_configs"] = (
            aws_sdk_lambda.types.code_signing_config_list.deserialize_json(
                data["CodeSigningConfigs"]
            )
        )
    return out
