"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserProficienciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.user_id
    import aws_sdk_connect.types.user_proficiency_list


class UpdateUserProficienciesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "aws_sdk_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    user_proficiencies: (
        "aws_sdk_connect.types.user_proficiency_list.UserProficiencyList"
    )
    """<p>The proficiencies to be updated for the user. Proficiencies must first be associated to the user. You can do this using AssociateUserProficiencies API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserProficienciesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.user_proficiency_list

    out["UserProficiencies"] = (
        aws_sdk_connect.types.user_proficiency_list.serialize_json(
            value["user_proficiencies"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateUserProficienciesRequest:
    out: UpdateUserProficienciesRequest = {}  # type: ignore[typeddict-item]
    if "UserProficiencies" in data:
        import aws_sdk_connect.types.user_proficiency_list

        out["user_proficiencies"] = (
            aws_sdk_connect.types.user_proficiency_list.deserialize_json(
                data["UserProficiencies"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserProficienciesRequest.user_proficiencies required"
        )
    return out
