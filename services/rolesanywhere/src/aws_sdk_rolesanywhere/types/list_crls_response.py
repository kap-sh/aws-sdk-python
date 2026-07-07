"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListCrlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.crl_details


class ListCrlsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>"""
    crls: NotRequired["aws_sdk_rolesanywhere.types.crl_details.CrlDetails"]
    """<p>A list of certificate revocation lists (CRL). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCrlsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "crls" in value:
        import aws_sdk_rolesanywhere.types.crl_details

        out["crls"] = aws_sdk_rolesanywhere.types.crl_details.serialize_json(
            value["crls"]
        )
    return out


def deserialize_json(data: dict) -> ListCrlsResponse:
    out: ListCrlsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "crls" in data:
        import aws_sdk_rolesanywhere.types.crl_details

        out["crls"] = aws_sdk_rolesanywhere.types.crl_details.deserialize_json(
            data["crls"]
        )
    return out
