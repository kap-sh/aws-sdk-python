"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputSecurityGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_input_security_group
    import capo_medialive.types.__string


class ListInputSecurityGroupsResponse(TypedDict, closed=True):
    input_security_groups: NotRequired[
        "capo_medialive.types.__list_of_input_security_group.__listOfInputSecurityGroup"
    ]
    """List of input security groups"""
    next_token: NotRequired["capo_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputSecurityGroupsResponse) -> dict:
    out: dict = {}
    if "input_security_groups" in value:
        import capo_medialive.types.__list_of_input_security_group

        out["inputSecurityGroups"] = (
            capo_medialive.types.__list_of_input_security_group.serialize_json(
                value["input_security_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputSecurityGroupsResponse:
    out: ListInputSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "inputSecurityGroups" in data:
        import capo_medialive.types.__list_of_input_security_group

        out["input_security_groups"] = (
            capo_medialive.types.__list_of_input_security_group.deserialize_json(
                data["inputSecurityGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
