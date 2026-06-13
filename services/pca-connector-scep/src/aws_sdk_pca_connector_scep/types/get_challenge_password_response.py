"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetChallengePasswordResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.sensitive_string


class GetChallengePasswordResponse(TypedDict):
    password: NotRequired[
        "aws_sdk_pca_connector_scep.types.sensitive_string.SensitiveString"
    ]
    """<p>The SCEP challenge password.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChallengePasswordResponse) -> dict:
    out: dict = {}
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> GetChallengePasswordResponse:
    out: GetChallengePasswordResponse = {}  # type: ignore[typeddict-item]
    if "Password" in data:
        out["password"] = data["Password"]
    return out
