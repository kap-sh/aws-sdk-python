"""Generated from Smithy shape ``com.amazonaws.vpclattice#BatchUpdateRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.rule_update_list
    import aws_sdk_vpc_lattice.types.service_identifier


class BatchUpdateRuleRequest(TypedDict):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""
    rules: "aws_sdk_vpc_lattice.types.rule_update_list.RuleUpdateList"
    """<p>The rules for the specified listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.rule_update_list

    out["rules"] = aws_sdk_vpc_lattice.types.rule_update_list.serialize_json(
        value["rules"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateRuleRequest:
    out: BatchUpdateRuleRequest = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import aws_sdk_vpc_lattice.types.rule_update_list

        out["rules"] = aws_sdk_vpc_lattice.types.rule_update_list.deserialize_json(
            data["rules"]
        )
    else:
        raise DeserializationError("BatchUpdateRuleRequest.rules required")
    return out
