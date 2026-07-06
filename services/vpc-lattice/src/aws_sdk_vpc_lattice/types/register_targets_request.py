"""Generated from Smithy shape ``com.amazonaws.vpclattice#RegisterTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_group_identifier
    import aws_sdk_vpc_lattice.types.target_list


class RegisterTargetsRequest(TypedDict, closed=True):
    target_group_identifier: (
        "aws_sdk_vpc_lattice.types.target_group_identifier.TargetGroupIdentifier"
    )
    """<p>The ID or ARN of the target group.</p>"""
    targets: "aws_sdk_vpc_lattice.types.target_list.TargetList"
    """<p>The targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterTargetsRequest) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.target_list

    out["targets"] = aws_sdk_vpc_lattice.types.target_list.serialize_json(
        value["targets"]
    )
    return out


def deserialize_json(data: dict) -> RegisterTargetsRequest:
    out: RegisterTargetsRequest = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import aws_sdk_vpc_lattice.types.target_list

        out["targets"] = aws_sdk_vpc_lattice.types.target_list.deserialize_json(
            data["targets"]
        )
    else:
        raise DeserializationError("RegisterTargetsRequest.targets required")
    return out
