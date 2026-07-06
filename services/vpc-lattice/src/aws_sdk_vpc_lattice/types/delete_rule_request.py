"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.rule_identifier
    import aws_sdk_vpc_lattice.types.service_identifier


class DeleteRuleRequest(TypedDict, closed=True):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""
    rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier"
    """<p>The ID or ARN of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleRequest:
    out: DeleteRuleRequest = {}  # type: ignore[typeddict-item]
    return out
