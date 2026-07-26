"""Generated from Smithy shape ``com.amazonaws.lambda#ListCodeSigningConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.code_signing_config_list
    import capo_lambda.types.string


class ListCodeSigningConfigsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""
    code_signing_configs: NotRequired[
        "capo_lambda.types.code_signing_config_list.CodeSigningConfigList"
    ]
    """<p>The code signing configurations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSigningConfigsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "code_signing_configs" in value:
        import capo_lambda.types.code_signing_config_list

        out["CodeSigningConfigs"] = (
            capo_lambda.types.code_signing_config_list.serialize_json(
                value["code_signing_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCodeSigningConfigsResponse:
    out: ListCodeSigningConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "CodeSigningConfigs" in data:
        import capo_lambda.types.code_signing_config_list

        out["code_signing_configs"] = (
            capo_lambda.types.code_signing_config_list.deserialize_json(
                data["CodeSigningConfigs"]
            )
        )
    return out
