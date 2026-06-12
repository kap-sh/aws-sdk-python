"""Generated from Smithy shape ``com.amazonaws.iot#ImplicitDeny``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.policies


class ImplicitDeny(TypedDict):
    policies: NotRequired["aws_sdk_iot.types.policies.Policies"]
    """<p>Policies that don't contain a matching allow or deny statement for the specified action on the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplicitDeny) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.serialize_json(value["policies"])
    return out


def deserialize_json(data: dict) -> ImplicitDeny:
    out: ImplicitDeny = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.deserialize_json(data["policies"])
    return out
