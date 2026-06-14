"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargetForm``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_name


class SubscriptionTargetForm(TypedDict):
    form_name: "aws_sdk_datazone.types.form_name.FormName"
    """<p>The form name included in the subscription target configuration.</p>"""
    content: "str"
    """<p>The content of the subscription target configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargetForm) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> SubscriptionTargetForm:
    out: SubscriptionTargetForm = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("SubscriptionTargetForm.form_name required")
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("SubscriptionTargetForm.content required")
    return out
