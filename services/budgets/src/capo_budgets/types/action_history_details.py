"""Generated from Smithy shape ``com.amazonaws.budgets#ActionHistoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.action
    import capo_budgets.types.generic_string


class ActionHistoryDetails(TypedDict, closed=True):
    message: "capo_budgets.types.generic_string.GenericString"
    action: "capo_budgets.types.action.Action"
    """<p>The budget action resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionHistoryDetails) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_budgets.types.action

    out["Action"] = capo_budgets.types.action.serialize_aws_json_1_1(value["action"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionHistoryDetails:
    out: ActionHistoryDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ActionHistoryDetails.message required")
    if "Action" in data:
        import capo_budgets.types.action

        out["action"] = capo_budgets.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("ActionHistoryDetails.action required")
    return out
