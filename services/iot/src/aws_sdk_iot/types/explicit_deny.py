"""Generated from Smithy shape ``com.amazonaws.iot#ExplicitDeny``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.policies


class ExplicitDeny(TypedDict, closed=True):
    policies: NotRequired["aws_sdk_iot.types.policies.Policies"]
    """<p>The policies that denied the authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExplicitDeny) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.serialize_json(value["policies"])
    return out


def deserialize_json(data: dict) -> ExplicitDeny:
    out: ExplicitDeny = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.deserialize_json(data["policies"])
    return out
