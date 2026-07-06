"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetDataLakePrincipalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.identity_string


class GetDataLakePrincipalResponse(TypedDict, closed=True):
    identity: NotRequired["aws_sdk_lakeformation.types.identity_string.IdentityString"]
    """<p>A unique identifier of the invoking principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataLakePrincipalResponse) -> dict:
    out: dict = {}
    if "identity" in value:
        out["Identity"] = value["identity"]
    return out


def deserialize_json(data: dict) -> GetDataLakePrincipalResponse:
    out: GetDataLakePrincipalResponse = {}  # type: ignore[typeddict-item]
    if "Identity" in data:
        out["identity"] = data["Identity"]
    return out
