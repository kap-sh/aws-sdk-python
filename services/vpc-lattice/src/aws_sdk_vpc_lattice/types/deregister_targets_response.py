"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeregisterTargetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.target_failure_list
    import aws_sdk_vpc_lattice.types.target_list


class DeregisterTargetsResponse(TypedDict):
    successful: NotRequired["aws_sdk_vpc_lattice.types.target_list.TargetList"]
    """<p>The targets that were successfully deregistered.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_vpc_lattice.types.target_failure_list.TargetFailureList"
    ]
    """<p>The targets that the operation couldn't deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterTargetsResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import aws_sdk_vpc_lattice.types.target_list

        out["successful"] = aws_sdk_vpc_lattice.types.target_list.serialize_json(
            value["successful"]
        )
    if "unsuccessful" in value:
        import aws_sdk_vpc_lattice.types.target_failure_list

        out["unsuccessful"] = (
            aws_sdk_vpc_lattice.types.target_failure_list.serialize_json(
                value["unsuccessful"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeregisterTargetsResponse:
    out: DeregisterTargetsResponse = {}  # type: ignore[typeddict-item]
    if "successful" in data:
        import aws_sdk_vpc_lattice.types.target_list

        out["successful"] = aws_sdk_vpc_lattice.types.target_list.deserialize_json(
            data["successful"]
        )
    if "unsuccessful" in data:
        import aws_sdk_vpc_lattice.types.target_failure_list

        out["unsuccessful"] = (
            aws_sdk_vpc_lattice.types.target_failure_list.deserialize_json(
                data["unsuccessful"]
            )
        )
    return out
