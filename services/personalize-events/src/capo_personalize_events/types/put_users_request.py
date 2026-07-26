"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_events.types.arn
    import capo_personalize_events.types.user_list


class PutUsersRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize_events.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Users dataset you are adding the user or users to.</p>"""
    users: "capo_personalize_events.types.user_list.UserList"
    """<p>A list of user data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutUsersRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    import capo_personalize_events.types.user_list

    out["users"] = capo_personalize_events.types.user_list.serialize_json(
        value["users"]
    )
    return out


def deserialize_json(data: dict) -> PutUsersRequest:
    out: PutUsersRequest = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("PutUsersRequest.dataset_arn required")
    if "users" in data:
        import capo_personalize_events.types.user_list

        out["users"] = capo_personalize_events.types.user_list.deserialize_json(
            data["users"]
        )
    else:
        raise DeserializationError("PutUsersRequest.users required")
    return out
