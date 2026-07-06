"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.service_identifier


class UpdateListenerRequest(TypedDict, closed=True):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""
    default_action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction"
    """<p>The action for the default rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateListenerRequest) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.rule_action

    out["defaultAction"] = aws_sdk_vpc_lattice.types.rule_action.serialize_json(
        value["default_action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateListenerRequest:
    out: UpdateListenerRequest = {}  # type: ignore[typeddict-item]
    if "defaultAction" in data:
        import aws_sdk_vpc_lattice.types.rule_action

        out["default_action"] = aws_sdk_vpc_lattice.types.rule_action.deserialize_json(
            data["defaultAction"]
        )
    else:
        raise DeserializationError("UpdateListenerRequest.default_action required")
    return out
