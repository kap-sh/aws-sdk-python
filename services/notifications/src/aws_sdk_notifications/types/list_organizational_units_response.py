"""Generated from Smithy shape ``com.amazonaws.notifications#ListOrganizationalUnitsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.organizational_units


class ListOrganizationalUnitsResponse(TypedDict):
    organizational_units: (
        "aws_sdk_notifications.types.organizational_units.OrganizationalUnits"
    )
    """<p>The list of organizational units that match the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The token to use for the next page of results. If there are no additional results, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationalUnitsResponse) -> dict:
    out: dict = {}
    import aws_sdk_notifications.types.organizational_units

    out["organizationalUnits"] = (
        aws_sdk_notifications.types.organizational_units.serialize_json(
            value["organizational_units"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationalUnitsResponse:
    out: ListOrganizationalUnitsResponse = {}  # type: ignore[typeddict-item]
    if "organizationalUnits" in data:
        import aws_sdk_notifications.types.organizational_units

        out["organizational_units"] = (
            aws_sdk_notifications.types.organizational_units.deserialize_json(
                data["organizationalUnits"]
            )
        )
    else:
        raise DeserializationError(
            "ListOrganizationalUnitsResponse.organizational_units required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
