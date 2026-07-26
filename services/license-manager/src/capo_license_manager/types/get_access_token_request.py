"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.max_size3_string_list
    import capo_license_manager.types.token_string


class GetAccessTokenRequest(TypedDict, closed=True):
    token: "capo_license_manager.types.token_string.TokenString"
    """<p>Refresh token, encoded as a JWT token.</p>"""
    token_properties: NotRequired[
        "capo_license_manager.types.max_size3_string_list.MaxSize3StringList"
    ]
    """<p>Token properties to validate against those present in the JWT token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessTokenRequest) -> dict:
    out: dict = {}
    out["Token"] = value["token"]
    if "token_properties" in value:
        import capo_license_manager.types.max_size3_string_list

        out["TokenProperties"] = (
            capo_license_manager.types.max_size3_string_list.serialize_aws_json_1_1(
                value["token_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessTokenRequest:
    out: GetAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "Token" in data:
        out["token"] = data["Token"]
    else:
        raise DeserializationError("GetAccessTokenRequest.token required")
    if "TokenProperties" in data:
        import capo_license_manager.types.max_size3_string_list

        out["token_properties"] = (
            capo_license_manager.types.max_size3_string_list.deserialize_aws_json_1_1(
                data["TokenProperties"]
            )
        )
    return out
