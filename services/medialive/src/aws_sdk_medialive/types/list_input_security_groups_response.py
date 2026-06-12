"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputSecurityGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_security_group
    import aws_sdk_medialive.types.__string


class ListInputSecurityGroupsResponse(TypedDict):
    input_security_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_security_group.__listOfInputSecurityGroup"
    ]
    """List of input security groups"""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputSecurityGroupsResponse) -> dict:
    out: dict = {}
    if "input_security_groups" in value:
        import aws_sdk_medialive.types.__list_of_input_security_group

        out["inputSecurityGroups"] = (
            aws_sdk_medialive.types.__list_of_input_security_group.serialize_json(
                value["input_security_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputSecurityGroupsResponse:
    out: ListInputSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "inputSecurityGroups" in data:
        import aws_sdk_medialive.types.__list_of_input_security_group

        out["input_security_groups"] = (
            aws_sdk_medialive.types.__list_of_input_security_group.deserialize_json(
                data["inputSecurityGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
