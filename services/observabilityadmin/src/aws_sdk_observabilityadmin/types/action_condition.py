"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ActionCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.action


class ActionCondition(TypedDict, closed=True):
    action: NotRequired["aws_sdk_observabilityadmin.types.action.Action"]
    """<p> The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED_AS_COUNT). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionCondition) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_observabilityadmin.types.action

        out["Action"] = aws_sdk_observabilityadmin.types.action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> ActionCondition:
    out: ActionCondition = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_observabilityadmin.types.action

        out["action"] = aws_sdk_observabilityadmin.types.action.deserialize_json(
            data["Action"]
        )
    return out
